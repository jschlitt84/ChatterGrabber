import nltk
import sys
import unicodedata
import cPickle

import sklearn
import nltk.classify.util

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from os.path import isfile
from random import shuffle
from numpy import mean, std
from copy import deepcopy
from pandas import read_csv
from multiprocessing import Process, Queue, cpu_count
from math import ceil

#Analysis methods from: 
#http://www.slideshare.net/ogrisel/nltk-scikit-learnpyconfr2010ogrisel#btnPrevious
#http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
#n-gram generation
#http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/

textColumn = 'text'
categoryColumn = 'check1'
defaultFile = 'nlpTrainers/NLTK_Ready_Tweets.csv'
cutoff = .75
resultKey = {1:"Category 1",2:"Category 2",3:"Category 3"}
stopWords = stopwords.words('english')
lmtzr = WordNetLemmatizer()

def stripUnicode(text):
    """Strips unicode special characters for text storage (smileys, etc)"""
    if text == None:
        return "NaN"
    else:
        if type(text) == unicode:
            return str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore'))
        else:
            return str(text)

def loadFile(text):
    outPut = []
    if text == "null":
        text = defaultFile
    if type(text) is list:
        fileIn = open('nlpTrainers/'+text[1],'rU')
    else:
        fileIn = open('nlpTrainers/'+text,'rU')

    loaded = read_csv(fileIn)
    
    for pos in loaded.index:
        outPut.append({'text': loaded[textColumn][pos], 'category': loaded[categoryColumn][pos]})
    
    print "Loaded",len(outPut),"entries"
    return outPut
    

def lemList(listed):
    listed = list(set([lmtzr.lemmatize(word) for word in listed if len(word)>1]))
    
    
def prepText(content):
    for pos in range(len(content)):
        content[pos]['text'] = prepTweet(content[pos]['text'])
    return content
        
        
def prepTweet(word):
    word =  stripUnicode(word)
    original = text = str(word)
    
    text = text.replace("&amp",'') #cleanup conversion bug
    
    punctuations = ".,\"-_%!?=+\n\t:;()*&$"
    
    """for char in punctuations:
        text = text.replace(char,' ')
    while '  ' in text:
        text = text.replace('  ',' ')
    while text.startswith(' '):
        text = text[1:]
    while text.endswith(' '):
        text = text[:-1]"""
    
    #Remove accentuated characters
    text = unicode(text)
    text = ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
        
    #End of string operations, continuing with list ops.    
    listed = text.lower().split(' ')
    
    for pos in range(len(listed)):
        if not listed[pos].startswith('http'):
            for char in punctuations:
                text = listed[pos].replace(char,' ')
                while '  ' in text:
                    text = text.replace('  ',' ')
                while text.startswith(' '):
                    text = text[1:]
                while text.endswith(' '):
                    text = text[:-1]
            listed[pos] = text
        
    if "@" in original: #track presence of conversations but remove screen names
        listed = [word for word in listed if '@' not in word]
        listed.append('@user')
        
    if "http" in original: #track presence of conversations but remove screen names
        listed = [word for word in listed if not word.startswith('http')]
        listed.append('$link')
        
    lemList(listed) #Lemmatize list to common stem words
    
    listed = [word for word in listed if word not in stopWords]  
    
    return listed
    
        
def prepClassifications(content):
    classifications = set()
    totals = dict()
    prepped = dict()
    
    for entry in content:
        category = str(entry['category'])
        classifications.add(category)
        if category not in totals.keys():
            totals[category] = 0
        totals[category] += 1
        
    print "Unique classifications found:",classifications 
    print "Occurrences:", totals
        
    prepped = dict()
    for classification in classifications:
        prepped[classification] = [entry for entry in content if str(entry['category']) == classification]
    return prepped
    
    
def getNGrams(listed, degreesUsed):
    NGrams = dict()
    for degree in degreesUsed:
        NGrams.update(dict([(ngram, True) for ngram in zip(*[listed[i:] for i in range(degree)])]))
    return NGrams
    
    
def collectNGrams(categorized, degreesUsed):
    collected = dict()
    for key in categorized.keys():
        collected[key] = [(getNGrams(entry['text'], degreesUsed),entry['category']) for entry in categorized[key]]
    return collected
                                             
 
def classifySingle(text, classifier,degreesToUse):
    temp = getNGrams(prepTweet(text),degreesToUse)
    if classifier['mode'] != 'svm':
        result = classifier['class'].classify(temp)
        return str(result)
    else:
        for category in classifier['priority']:
            if classifier['class'][category].classify(temp):
                return str(category)
        return classifier['priority'][-1]


def prepSVMClass(data, category, mode, value):
    posData = [entry for entry in deepcopy(data) if str(entry[-1]) == str(category)]
    negData = [entry for entry in deepcopy(data) if str(entry[-1]) != str(category)]
    shuffle(negData)
    if mode == 'number':
        negData = negData[:value]
    elif mode == 'ratio':
        negData = negData[:int(len(posData)*value)]   
    posData = [entry[:-1] + (True,) for entry in posData]
    negData = [entry[:-1] + (False,) for entry in negData]
    strData = ','.join(str(item) for item in (posData+negData))
    return {'pos':posData,'neg':negData,'strData':strData}


def prepSVMAll(readyToSend,priority,allCats,cfg):
    import nltk.classify
    from sklearn.svm import LinearSVC
    from nltk.classify import SklearnClassifier
    trainingSets = dict()
    classifiers = dict()
    mode = cfg['SVMMode']
    value = cfg['SVMNumber']
    print "Pulling data for SVM categories"
    for category in allCats:
        temp = prepSVMClass(readyToSend, category, mode, value)
        trainingSets[category] = temp['pos'] + temp['neg']
    print "Training SVM classifiers"
    for category in allCats:
        classifiers[category] = SklearnClassifier(LinearSVC()).train(trainingSets[category])
    return classifiers
             
                         
def getClassifier(tweetfile,cfg):
    degreesToUse = cfg['NLPnGrams']
    classMode = cfg['NLPMode']
    shortClass = classMode.replace(' ','').lower()
    loadNeeded = True 

    if 'NLPTEST' not in cfg.keys():
	degreeString = '-'.join([str(degree) for degree in degreesToUse])
        pickleFile = 'nlpTrainers/'+tweetfile.replace('.csv','.'+shortClass+degreeString+'.pickle')  
	if isfile(pickleFile):
		print "Loading pickled", shortClass, "classifier"
		fileIn = open(pickleFile)
		classifier = cPickle.load(fileIn)
		fileIn.close()
		loadNeeded = False
    
    if loadNeeded:
        if 'NLPTEST'in cfg.keys():
            content = prepText(tweetfile)
            categorized = prepClassifications(content)
            NGrammized = collectNGrams(categorized,degreesToUse)
        else:
            print "Loading content & preparing text"
            content = prepText(loadFile(tweetfile))
            print "Categorizing contents"
            categorized = prepClassifications(content)
            print "Deriving NGrams of length(s)", degreesToUse
            NGrammized = collectNGrams(categorized,degreesToUse)
            print "Compiling Results"
        readyToSend = []
        allCats = [str(key) for key in NGrammized.keys()]
        for category in allCats:
            readyToSend += NGrammized[category]
            
        print "Attempting Classification by mode", classMode, degreesToUse
        if classMode == 'naive bayes':
            from nltk.classify import NaiveBayesClassifier
            classifier = {'class':NaiveBayesClassifier.train(readyToSend),'mode':'nb'}
        elif classMode == 'positive naive bayes':
            from nltk.classify import PositiveNaiveBayesClassifier
            classifier = {'class':PositiveNaiveBayesClassifier.train(readyToSend,algorithm='iis'),'mode':'pnb'}
        elif classMode == 'max ent':
            from nltk.classify import MaxentClassifier
            classifier = {'class':MaxentClassifier.train(readyToSend),'mode':'me'}
        elif classMode == 'decision tree':
            from nltk.classify import DecisionTreeClassifier
            classifier = {'class':DecisionTreeClassifier.train(readyToSend),'mode':'dt'}
        elif classMode == 'svm':
            if "SVMOrder" in cfg.keys():
                priority =  cfg['SVMOrder']
            else:
                priority =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ9876543210"
            if type(priority) is str:
                priority = list(priority)
            priority = [entry for entry in priority if entry in allCats]
            preppedSVM = prepSVMAll(readyToSend,priority,allCats,cfg)
            classifier = {'class':preppedSVM,'mode':'svm','priority':priority}
	else:
	    from nltk.classify import NaiveBayesClassifier
            classifier = {'class':NaiveBayesClassifier.train(readyToSend),'type':'nb'}
        
        if 'NLPTEST' not in cfg.keys():
            print "Pickling Classifier"
            fileOut = open(pickleFile, 'wb')
            cPickle.dump(classifier, fileOut)
            fileOut.close() 
              
    if 'NLPTEST' not in cfg.keys():
        
        classifier.show_most_informative_features(n=150)
    
    return classifier

            
def getAccuracy(toRun,mode,degrees,n,percent,classifications,outPut,cfg,core,out_q):
    sens = dict()
    spec = dict()
    outDict = dict()
    sensDelta = dict()
    specDelta = dict()
    sensScores = dict()
    specScores = dict()
    totals = dict()
    
    allCats = deepcopy(classifications)
    
    for category in allCats:
        sensScores[category] = []
        specScores[category] = []
    
    scored = len(outPut)
    index = range(scored)
    percentLength = int(scored*percent+.5)
    remainder = scored - percentLength
    
    print "\033[1mReducing scoring set of size %s to %s%% random training set with %s entries for %s iterations and %s scored posts\033[0m\n" % (scored,percent*100,percentLength,n,remainder)	
        
    for iteration in toRun:
        shuffle(index)
        points = 100
        
        trainingSet = deepcopy(index)[0:percentLength]
        scoringSet = list(set(index)-set(trainingSet))
        toTrain = [deepcopy(outPut[item]) for item in trainingSet]
        toScore = [deepcopy(outPut[item]) for item in scoringSet]
        
        classifications = set()
        
        for category in allCats:
            totals[category] = 0
        
        for entry in toScore:
            category = str(entry['category'])
            classifications.add(category)
            if category not in totals.keys():
                totals[category] = 1
            totals[category] += 1
            
        allCount = sum(totals.values())
        
        for category in allCats:
            sens[category] = 100.
            spec[category] = 100.
            if totals[category] != 0:          
                sensDelta[category] = 100./totals[category]
            else:
                sensDelta[category] = 'no one will ever see this...'
            specDelta[category] = 100./(allCount-totals[category])
          
        subtractor =  100./allCount
        if type(cfg) != dict:
            cfg = dict()
        cfg['NLPnGrams'] = degrees
        cfg['NLPMode'] = mode
        cfg['NLPTEST'] = True
        
        classifier = getClassifier(toTrain,cfg)
        for item in toScore:
            realCat = str(item['category'])
            scoreCat = str(classifySingle(item['text'],classifier,degrees))
            if realCat != scoreCat:
                points -= subtractor
                sens[realCat] -= sensDelta[realCat]
                spec[scoreCat] -= specDelta[scoreCat]
        
        outDict['scores'+str(iteration)] = points
        outDict['toTrain'+str(iteration)] =len(trainingSet)
        
        for category in classifications:
            outDict['sensScores'+'_'+category+'_'+str(iteration)]  = sens[category]
            outDict['specScores'+'_'+category+'_'+str(iteration)]  = spec[category]
    
       
    out_q.put(outDict)
    
                                                
            
def evalAccuracy(mode,degrees,n,percent,cores,classifications,outPut,cfg):
    sensScores = dict()
    specScores = dict()
    scores = []
    merged = {}
    
    allCats = deepcopy(classifications)
    coreSweep = range(cores)
    
    iterationNumber = range(n)
    out_q = Queue()
    block =  int(ceil(n/float(cores)))
    processes = []
    toDel = []
    
    for i in range(cores):
        toSend = iterationNumber[block*i:block*(i+1)]
        if len(toSend) != 0:
            p = Process(target = getAccuracy, args = (iterationNumber[block*i:block*(i+1)], mode,degrees,n,percent,classifications,outPut,cfg,cores,out_q))
            processes.append(p)
            p.start()
        else:
            toDel.append(i)
    
    coreSweep = [entry for entry in coreSweep if entry not in toDel]
    
    for i in coreSweep:
        merged.update(out_q.get())
    for p in processes:
        p.join()
        
    for category in allCats:
        sensScores[category] = []
        specScores[category] = []
    
    for i in range(n):
        scores.append(merged['scores'+str(i)])
        for category in allCats:
            sensScores[category].append(merged['sensScores'+'_'+category+'_'+str(i)])
            specScores[category].append(merged['specScores'+'_'+category+'_'+str(i)])
    
    for category in allCats:
        sensScores[category] = mean(sensScores[category])
        specScores[category] = mean(specScores[category])
    
    return mean(scores),std(scores),percent,merged['toTrain0'],sensScores,specScores



def main(tweetfile):
    testMode = False
    try:
        if sys.argv[1] == 'test':
            testMode = True
    except:
        testMode = False
        
    classifier = getClassifier(tweetfile)
    
    if testMode:
        print "\nInitiating testing mode\n"
        while True:
            query = str(raw_input("Please enter a test sentence: \t"))
            if query.lower() == 'quit':
                quit()
            classifySingle(query, classifier)
            
 
                       
if __name__ == '__main__':
    main(sys.argv[2])
