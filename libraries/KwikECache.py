from cPickle import load,dump
from os import path
from time import sleep

import random
import optimizeClassifier

def updateCache(dictionary,fileRef,limit,expectDict = True):
    """Updates file & memory version of cache"""
    loadedLength = length1 = len(dictionary.keys())
    pickleExists = path.isfile(fileRef)
    badDict = badPickle = False
    if expectDict and type(dictionary) is not dict:
        print "Error, expected dictionary [out], type is", type(dictionary)
        dictionary = dict()
        badDict = True
    if pickleExists:
        pickleLoaded = loadWhenReady(fileRef,dictionary)
        if expectDict and type(pickleLoaded) is not dict:
            badPickle = True
            print "Error, expected dictionary [in], type is", type(pickleLoaded)
        if badDict and badPickle:
            print "Double error, setting dictionary to empty"
        elif badDict:
            dictionary.update(pickleLoaded)
        elif badPickle:
            needsWrite = True
        else:
            length1 = len(pickleLoaded.keys())
            if dictionary.keys() != pickleLoaded.keys():
                dictionary.update(pickleLoaded)
                needsWrite = True
            else:
                needsWrite = False
    else:
        needsWrite = True
    length2 = len(dictionary.keys())
    if needsWrite and loadedLength != 0 or (length2-length1) > limit:
        print "Updating master cache,", length2-length1,"new entries added with",length2,"total in cache"
        dumpWhenReady(fileRef,dictionary)
        sleep(.5)



def getNLPScore(cacheKey,cache,cacheRef,args,updateLimit):
	if cacheKey in cache.keys():
		print "Returning score", cache[cacheKey], "from cache"
                return cache[cacheKey]
        cache[cacheKey] = temp = float(optimizeClassifier.main(args,'mendel'))
        updateCache(cache,cacheRef,updateLimit)
        return temp



"""def openWhenReady(directory, mode):
    #Trys to open a file, if unable, waits five seconds and tries again
    attempts = 0
    while True:
        try:
            sleep(2 * random.random())
            fileOut = open(directory,mode)
            break
        except:
            sleep(5)
            attempts += 1
            if attempts == 1000:
                print "Error: Unable to open", directory, "for 5000 seconds, quiting now"
                quit()
    return fileOut"""
    
    
    
def loadWhenReady(fileRef,dictionary):
    """Trys to load a pickle, if unable, waits five seconds and tries again"""
    attempts = 0
    while True:
        try:
            sleep(10 * random.random())
            pickleIn = open(fileRef,'rb')
            pickleLoaded = load(pickleIn)
            pickleIn.close()
            break
        except:
            sleep(5)
            attempts += 1
            if attempts == 3:
                print "Error: Unable to load pickle, corrupted?"
                if len(dictionary.keys())>1000:
                    print "Dumping memory dictionary instead"
                    dumpWhenReady(fileRef,dictionary)
                    return dictionary
                else:
                    print "None in memory either... quitting now"
                    quit()
    return pickleLoaded
    
    

def dumpWhenReady(fileRef, dictionary):
    """Trys to dump a pickle, if unable, waits five seconds and tries again"""
    attempts = 0
    while True:
        try:
            sleep(2 * random.random())
            pickleOut = open(fileRef, "wb")
            dump(dictionary, pickleOut,protocol=2)
            pickleOut.close()
            sleep(2)
            break
        except:
            sleep(5)
            attempts += 1
            if attempts == 1000:
                print "Error: Unable to open pickle, quiting now"
                quit()

