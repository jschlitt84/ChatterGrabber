import nltk
import csv
import sys
import unicodedata
import pandas as pd
import urllib
import pickle
import cPickle

import nltk.classify.util
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from os.path import isfile
from random import shuffle
from numpy import mean, std
from copy import deepcopy

#Analys Methods from: 
#http://www.slideshare.net/ogrisel/nltk-scikit-learnpyconfr2010ogrisel#btnPrevious
#http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
#n-gram generation
#http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/

textColumn = 'text'
categoryColumn = 'check1'
defaultFile = 'nlpTrainers/NLTK_Ready_Tweets.csv'
cutoff = .75
resultKey = {1:"Category 1",2:"Category 2",3:"Category 3"}



def stripUnicode(text):
    """Strips unicode special characters for text storage (smileys, etc)"""
    if text == None:
        return "NaN"
    else:
        if type(text) == unicode:
            return str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore'))
        else:
            return text

def loadFile(text):
    outPut = []
    if text == "null":
        text = defaultFile
    if type(text) is list:
        fileIn = open('nlpTrainers/'+text[1],'rU')
    else:
        fileIn = open('nlpTrainers/'+text,'rU')

    loaded = pd.read_csv(fileIn)
    
    for pos in loaded.index:
        outPut.append({'text': loaded[textColumn][pos], 'category': loaded[categoryColumn][pos]})
    
    print "Loaded",len(outPut),"entries"
    return outPut
    

def lemList(listed):
    lmtzr = WordNetLemmatizer()
    listed = [word for word in listed if len(word)>1]
    for pos in range(len(listed)):
        listed[pos] = lmtzr.lemmatize(listed[pos])
        
    
def prepText(content):
    for pos in range(len(content)):
        content[pos]['text'] = prepTweet(content[pos]['text'])
    return content
        
        
def prepTweet(word):
    
    word =  stripUnicode(word)
    original = text = str(word)
    
    text = text.replace("&amp",'&') #cleanup conversion bug
    
    punctuations = ".,\"-_%!=+\n\t:;()*&$"
    
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
    listed = text.split(' ')
    
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
            listed[pos] = text.lower()
        """else:
            linked = urllib.urlopen(listed[pos])
            if linked.getcode() == 200:
                listed[pos] = linked.url"""
        
    if "@" in original: #track presence of conversations but remove screen names
        listed = [word for word in listed if '@' not in word]
        listed.append('@user')
        
    lemList(listed) #Lemmatize list to common stem words
    
    stop = stopwords.words('english') #Remove stopwords, common words of little relevance
    listed = [word for word in listed if word not in stop]  
    
    return listed
    
        
def prepClassifications(content):
    classifications = set()
    totals = dict()
    prepped = dict()
    
    for entry in content:
        category = entry['category']
        classifications.add(category)
        if category not in totals.keys():
            totals[category] = 0
        totals[category] += 1
        
    print "Unique classifications found:",classifications 
    print "Occurrences:", totals
        
    prepped = dict()
    for classification in classifications:
        prepped[classification] = [entry for entry in content if entry['category'] == classification]
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
    result = classifier.classify(temp)
    if __name__ == '__main__':
        print "Query:", text
        try:
            print "Result:", resultKey[result]
        except:
            print "Result:", result
    return str(result)
     
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
        for category in NGrammized.keys():
            readyToSend += NGrammized[category]
            
        print "Attempting Classification by mode", classMode, degreesToUse
        if classMode == 'naive bayes':
            from nltk.classify import NaiveBayesClassifier
            classifier = NaiveBayesClassifier.train(readyToSend)
        elif classMode == 'max ent':
            from nltk.classify import MaxentClassifier
            classifier = MaxentClassifier.train(readyToSend)
        elif classMode == 'decision tree':
            from nltk.classify import decisiontree
            classifier = decisiontree.train(readyToSend)
	else:
	    from nltk.classify import NaiveBayesClassifier
            classifier = NaiveBayesClassifier.train(readyToSend)
        
        if 'NLPTEST' not in cfg.keys():
            print "Pickling Classifier"
            fileOut = open(pickleFile, 'wb')
            cPickle.dump(classifier, fileOut)
            fileOut.close() 
              
    if 'NLPTEST' not in cfg.keys():
        
        classifier.show_most_informative_features(n=150)
    
    return classifier

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
            
            
def evalAccuracy(tweetFile,mode,degrees,percent):
    outPut = []
    pieces = []
    remainders = []
    segments = 10
    accuracy = []
    
    if tweetFile == "null":
        text = defaultFile
    else:
        fileIn = open(tweetFile,'rU')

    loaded = pd.read_csv(fileIn)
    
    for pos in loaded.index:
        outPut.append({'text': loaded[textColumn][pos], 'category': loaded[categoryColumn][pos]})

    scored = len(outPut)
    index = range(scored)
    percentLength = int(scored*percent+.5)
    chunkSize = percentLength/segments
    reducedSize = chunkSize*segments
    shuffle(index)
    index = index[:reducedSize]
    pieces = zip(*[iter(index)]*chunkSize)
    print "Reducing set of size %s to percent %s to size %s with %s total pieces of size %s each" % (scored,percent*100,reducedSize,segments,chunkSize)	
    scores = []
    for pos in range(segments):
        entry = pieces[pos]
        remainder = list(set(index)-set(entry))
        toTrain = [deepcopy(outPut[item]) for item in remainder]
        toScore = [deepcopy(outPut[item]) for item in entry]
        points = 100
        subtractor =  100./chunkSize
        cfg = {'NLPnGrams':degrees,'NLPMode':mode,'NLPTEST':True}
        classifier = getClassifier(toTrain,cfg)
        for item in toScore:
            if str(item['category']) != str(classifySingle(item['text'],classifier,degrees)):
                points -= subtractor
        scores.append(points)
    return mean(scores),std(scores)
        
            
    
    print "Loaded & randomized %s entries, reduced to %s entries with %s chunks of size %s" % (scored,reducedSize,segments,chunkSize)
    return outPut
    


if __name__ == '__main__':
    main(sys.argv[2])
