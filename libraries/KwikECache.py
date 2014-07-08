from cPickle import load,dump
from os import path
from time import sleep

import optimizeClassifier

def updateCache(dictionary,fileRef,limit):
    """Updates file & memory version of cache"""
    loadedLength = length1 = len(dictionary.keys())
    pickleExists = path.isfile(fileRef)
    if pickleExists:
        pickleIn = openWhenReady(fileRef, "rb")
        pickleLoaded = load(pickleIn)
        length1 = len(pickleLoaded.keys())
        pickleIn.close()
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
        pickleOut = openWhenReady(fileRef,"wb")
        dump(dictionary, pickleOut)
        pickleOut.close()
        sleep(.5)



def getNLPScore(cacheKey,cache,cacheRef,args,updateLimit):
	if cacheKey in cache.keys():
		print "Returning score", cache[cacheKey], "from cache"
                return cache[cacheKey]
        cache[cacheKey] = temp = float(optimizeClassifier.main(args,'mendel'))
        updateCache(cache,cacheRef,updateLimit)
        return temp



def openWhenReady(directory, mode):
    """Trys to open a file, if unable, waits five seconds and tries again"""
    attempts = 0
    while True:
        try:
            fileOut = open(directory,mode)
            break
        except:
            sleep(5)
            attempts += 1
            if attempts == 1000:
                print "Error: Unable to open", directory, "for 5000 seconds, quiting now"
                quit()
    return fileOut
