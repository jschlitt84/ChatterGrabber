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
        if len(str(loaded[categoryColumn][pos])) != 0 and str(loaded[categoryColumn][pos]) != 'nan':
            temp = loaded[categoryColumn][pos]
            try:
                if int(temp) == float(temp):
                    temp = str(int(temp))
                else:
                    temp = str(temp)
            except:
                temp = str(temp)
                    
            outPut.append({'text': loaded[textColumn][pos], 'category': temp})
    
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
    toAdd = set()
    
    #if text[0] == '"' and text[-1] == '"' or   text[0] == "'" and text[-1] == "'":
    #    toAdd.add('$isQuote')
    #elif text.count('"') > 1 or text.count("'") > 1:
    #    toAdd.add('$hasQuote')
    #if text.isupper():
    #    toAdd.add('$allCaps')
        
    if '?' in text:
	toAdd.add('$?')
    if '!' in text:
	toAdd.add('$!')
    if '...' in text:
	toAdd.add('$...')

    punctuations = ".,\"-_%!?=+\n\t:;()*&$/"
    
    #Remove accentuated characters
    text = unicode(text)
    text = ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
        
    #End of string operations, continuing with list ops.    
    

    while 'http' in text:
	toAdd.add('$link')
	temp = text.index('http')
	text = text[:temp] + text[text.find(' ',temp):]
    while 'RT @' in text:
	toAdd.add('$RT')
	temp = text.index('RT @')
	text = text[:temp] + text[text.find(' ',temp):]
    while '@' in text:
	toAdd.add('@user')
	temp = text.index('@')
	if temp == len(text) - 1:
		text = text[:-1]
	else:
		text = text[:temp] + text[text.find(' ',temp):]
    for char in punctuations:
	text = text.replace(char,' ')
    while '  ' in text:
        text = text.replace('  ',' ')
    while text.startswith(' '):
        text = text[1:]
    while text.endswith(' '):
        text = text[:-1]
    listed = text.lower().split(' ')
    
    wordCount = len(listed)
    wordLength = int(mean([len(word) for word in listed])+.5)
    
    #toAdd.add('$wordCount'+str(wordCount))
    #toAdd.add('$wordLength'+str(wordLength))
   
        
    lemList(listed) #Lemmatize list to common stem words
    
    toDel = set()
    for word in listed:
	try:
	     temp = float(word)
	     toDel.add(word)
	     if int(temp) == temp:
		toAdd.add("$int")
	     else:
		toAdd.add("$float")
	except:
	     None

    listed = [word for word in [word for word in listed if word not in stopWords] if word not in toDel] + list(toAdd) 
    
    return listed
    
 
def getTotals(content):
    classifications = set()
    totals = dict()
    for entry in content:
        category = str(entry['category'])
        classifications.add(category)
        if category not in totals.keys():
            totals[category] = 0
        totals[category] += 1
        
    print "Unique classifications found:",classifications 
    print "Occurrences:", totals
        
    return totals,classifications
            
                      
def prepClassifications(content):
    totals,classifications =  getTotals(content) 
    prepped = dict()
    for classification in classifications:
        prepped[classification] = [entry for entry in content if str(entry['category']) == classification]
    return prepped
    
    
def getNGrams(listed, degreesUsed):
    NGrams = dict()
    for degree in degreesUsed:
        NGrams.update(dict([(ngram, True) for ngram in zip(*[listed[i:] for i in range(degree)])]))
    return NGrams

def cleanNGrams(nGrams, degreesUsed, minFreq):
    if type(minFreq) is int:
        tempFreq = [minFreq]* len(degreesUsed)
    else:
        tempFreq = degreesUsed
        
    for pos in min(len(degreesUsed,tempFreq)):
        current = tempFreq[pos]
        found = dict()
        for entry in nGrams:
            print entry
            quit() 
    
def collectNGrams(categorized, degreesUsed, cfg):
    collected = dict()
    if "NLPFreqLimit" in cfg.keys():
	lengths = deepcopy(cfg['NLPFreqLimit'])
	if lengths == []:
	     lengths = [2] * len(degreesUsed)
	elif type(lengths) is int:
	     lengths = [lengths] * len(degreesUsed)
    else:
	lengths = [2]*len(degreesUsed)
    for key in categorized.keys():
        collected[key] = [(getNGrams(entry['text'], degreesUsed),entry['category']) for entry in categorized[key]]

    if sum(lengths) == len(lengths):
	return collected
    

    toTrim = [entry for entry in lengths[:min(len(lengths),len(degreesUsed))]]+max(len(degreesUsed)-len(lengths),0)*[2]    
    trimLevels = dict()
    for pos in range(len(toTrim)):
	trimLevels[degreesUsed[pos]] = toTrim[pos]

    counted = dict()
    gramCount = dict()    

    allRows = [item for catList in collected.values() for item in catList]
    allTuples = [item.keys() for tupleList in allRows for item in tupleList[:-1]]
    allKeys = [item for keyList in allTuples for item in keyList]
    print "Filtering nGrams by prevalence limits", trimLevels
    for pos in range(len(degreesUsed)):
	gramCount[degreesUsed[pos]] = []
	counted[degreesUsed[pos]] = dict()
    for key in allKeys:
	gramCount[len(key)].append(key)
    print "Counting nGram occurences"
    for key in list(set(allKeys)):
	counted[len(key)][key] = gramCount[len(key)].count(key)
    print "Selecting relevant nGrams"
    for key in counted.keys():
	counted[key] = set([key2 for key2,item in counted[key].iteritems() if item >= trimLevels[len(key2)]])
    print "Reducing scoring set"
    
    #print "deboo", len(collected['4'])
    for key in collected.keys():
	collected[key] = [(dict.fromkeys([key2 for key2 in entry[0].keys() if key2 in counted[len(key2)]],True),entry[1]) for entry in collected[key]]
	collected[key] = [item for item in collected[key] if len(item[0].keys()) != 0]
    #collected = [item for item in collected if len(item) >0]
    #print "deboo", len(collected['4'])
    #print collected['4']
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
        negData = negData[:int(value)]
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
    classMode = cfg['NLPMode'].replace('-',' ').replace('_',' ')
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
            NGrammized = collectNGrams(categorized,degreesToUse,cfg)
        else:
            print "Loading content & preparing text"
            content = prepText(loadFile(tweetfile))
            print "Categorizing contents"
            categorized = prepClassifications(content)
            print "Deriving NGrams of length(s)", degreesToUse
            NGrammized = collectNGrams(categorized,degreesToUse,cfg)
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
            classifier = {'class':PositiveNaiveBayesClassifier.train(readyToSend),'mode':'pnb'}
        elif classMode == 'max ent':
            #import nltk.classify
            #from sklearn.linear_model import LogisticRegression
            #from nltk.classify import SklearnClassifier
            #classifier = {'class':LogisticRegression.train(readyToSend),'mode':'me'}
            from nltk.classify import MaxentClassifier
            classifier = {'class':MaxentClassifier.train(readyToSend,algorithm='iis'),'mode':'me'}
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
            classifier = {'class':NaiveBayesClassifier.train(readyToSend),'mode':'nb'}
        
        if 'NLPTEST' not in cfg.keys():
            print "Pickling Classifier"
            fileOut = open(pickleFile, 'wb')
            cPickle.dump(classifier, fileOut)
            fileOut.close() 
              
    if 'NLPTEST' not in cfg.keys():
        if classMode != 'svm': 
        	classifier['class'].show_most_informative_features(n=150)
	"""else:
		for key in classifier['class'].keys():
			print classifier		
			print classifier.keys()
			classifier['class'][key].show_most_informative_features(n=150/len(classifier['class'].keys()))"""    
    
    return classifier

            
def getAccuracy(toRun,mode,degrees,n,percent,classifications,rOutput,cfg,core,out_q):
	if True:
	    sens = dict()
	    spec = dict()
	    outDict = dict()
	    sensDelta = dict()
	    specDelta = dict()
	    sensScores = dict()
	    specScores = dict()
	    
	    allCats = deepcopy(classifications)
	    
	    for category in allCats:
		sensScores[category] = []
		specScores[category] = []
	    
	    scored = len(rOutput)
	    index = range(scored)
	    percentLength = int(scored*percent+.5)
	    remainder = scored - percentLength
	    
	    print "\033[1mReducing scoring set of size %s to %s%% random training set with %s entries for %s iterations and %s scored posts\033[0m\n" % (scored,percent*100,percentLength,n,remainder)	
	
	    for iteration in toRun:
                scoringSet = deepcopy(index)[iteration*remainder:(iteration+1)*remainder]	
		trainingSet = list(set(index)-set(scoringSet))
		
		toTrain = [deepcopy(rOutput[item]) for item in trainingSet]
		toScore = [deepcopy(rOutput[item]) for item in scoringSet]
		
		print "DEBOOF",len(toTrain),len(toScore),toRun,remainder,iteration
		print "DEBOOF2",len(scoringSet),len(trainingSet),toRun,remainder,iteration
		
		totals,classifications =  getTotals(toScore)
		    
		allCount = sum(totals.values())
		
		print "DEBOOTOTALs",totals
		for category in allCats:
		    sens[category] = 100.; spec[category] = 100.
		    if totals[category] != 0:          
		        sensDelta[category] = 100./totals[category]
		    else:
		        sensDelta[category] = 'no one will ever see this...'
		    specDelta[category] = 100./(allCount-totals[category])
		  
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
		        sens[realCat] -= sensDelta[realCat]
		        spec[scoreCat] -= specDelta[scoreCat]
		
		outDict['toTrain'+str(iteration)] = len(trainingSet)
		
		for category in classifications:
		    outDict['sensScores'+'_'+category+'_'+str(iteration)]  = sens[category]
		    outDict['specScores'+'_'+category+'_'+str(iteration)]  = spec[category]
	      
	    out_q.put(outDict)
	    
	else:
		print "Subprocesses failed, returning error, why is this crap not working!?!?!"
		outDict['failed'] = True
		out_q.put(outDict)
    
                                                
            
def evalAccuracy(mode,degrees,n,percent,cores,classifications,outPut,cfg):
    sensScores = dict(); specScores = dict()
    scores = []
    merged = {}
    
    allCats = deepcopy(classifications)
    coreSweep = range(cores)
    
    iterationNumber = range(n)
    out_q = Queue()
    block =  int(ceil(n/float(cores)))
    processes = []
    toDel = []
    rOutput = deepcopy(outPut)
    shuffle(rOutput) 
    for i in range(cores):
        toSend = iterationNumber[block*i:block*(i+1)]
        if len(toSend) != 0:
            p = Process(target = getAccuracy, args = (iterationNumber[block*i:block*(i+1)], mode,degrees,n,percent,classifications,rOutput,cfg,cores,out_q))
            processes.append(p)
            p.start()
        else:
            toDel.append(i)
    
    coreSweep = [entry for entry in coreSweep if entry not in toDel]
    
    for i in coreSweep:
        merged.update(out_q.get())
    for p in processes:
        p.join()

    if 'failed' in merged.keys():
	return 'failed'
        
    for category in allCats:
        sensScores[category] = []
        specScores[category] = []
    
    for i in range(n):
        scores.append(merged['scores'+str(i)])
        for category in allCats:
	    if ('sensScores'+'_'+category+'_'+str(i)) in merged.keys():
        	sensScores[category].append(merged['sensScores'+'_'+category+'_'+str(i)])
        	specScores[category].append(merged['specScores'+'_'+category+'_'+str(i)])
    print "DEBOO", sensScores, specScores
    for category in allCats:
        #print 'DEBOOO', category
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
