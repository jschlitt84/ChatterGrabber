import pandas as pd
import sys
import datetime
import csv

from GISpy import sanitizeTweet, outTime, zipData
from copy import deepcopy
from os import remove

indexKeys = ['text','created_at']
updateKeys = ['place','nltkCat','tweetType','geoType','lat','lon']



def makeKey(tweet,keyList):
    return ','.join([(entry+':'+str(tweet[entry])) for entry in keyList if entry in tweet.keys()])
    
    
def loadTweets(fileRef,cfg):
    loaded = pd.DataFrame.from_csv(fileRef,index_col='created_at')
    loaded = loaded.reset_index()
    indexed = dict()
    for pos in loaded.index:
        entry = dict(loaded.irow(pos))
        if cfg['Sanitize']:
            entry = sanitizeTweet(entry)
        indexed[makeKey(entry,indexKeys)] = entry
    return indexed
    
    
def addExtra(data,extraArgs):
    for key in data.keys():
        data[key].update(deepcopy(extraArgs))


def writeCSV(data, directory,name,timeStamp):
    reindexed = data.values()
    orderedKeys = sorted(reindexed[0].keys())
    outName = name + ' ' + timeStamp.replace(':','.') + '.csv'
    print "Writing collected tweets to '"+outName + "'"
    
    outFile = open(directory+outName, "w") 
    csvOut = csv.DictWriter(outFile,orderedKeys)
    csvOut.writer.writerow(orderedKeys)
    csvOut.writerows(reindexed)
    outFile.close()
    return directory + outName


def getDeltas(fileOld, fileNew, cfg):
    loadedNew = loadTweets(fileNew,cfg)
    timeList = [entry['created_at'] for entry in loadedNew.values()]
    minTime = min(timeList)
    
    loadedOld = {key:item for key, item in loadTweets(fileOld,cfg).iteritems() if item['created_at'] >= minTime}
    merged = deepcopy(loadedOld); merged.update(loadedNew)
    
    newKeys = set(loadedNew.keys())
    oldKeys = set(loadedOld.keys())
    
    addedKeys = newKeys.difference(oldKeys)
    removedKeys = oldKeys.difference(newKeys)
    sameKeys = newKeys.intersection(oldKeys)
    updatedKeys = set([entry for entry in sameKeys if makeKey(loadedNew[entry],updateKeys) != makeKey(loadedOld[entry],updateKeys)])
    
    timeStamp =  outTime(datetime.datetime.now())['full']
    
    if len(addedKeys) >= 1:
        addedData = {key:value for key,value in merged.iteritems() if key in addedKeys}
        addExtra(addedData,{'operation':'add','operationTime':timeStamp})
    if len(removedKeys) >= 1:
        removedData = {key:value for key,value in merged.iteritems() if key in removedKeys}
        addExtra(removedData,{'operation':'remove','operationTime':timeStamp})
    if len(updatedKeys) >= 1:
        updatedData = {key:value for key,value in merged.iteritems() if key in updatedKeys}
        addExtra(updatedData,{'operation':'updated','operationTime':timeStamp})
    
    fileLocs = [fileNew]
    fileLocs.append(writeCSV(addedData,'',"Added",timeStamp))
    fileLocs.append(writeCSV(removedData,'',"Removed",timeStamp))
    fileLocs.append(writeCSV(updatedData,'',"Updated",timeStamp))
    
    zipData(fileLocs,'',timeStamp)

cfg = {'Sanitize':False}
getDeltas('testOld.csv','testNew.csv',cfg)