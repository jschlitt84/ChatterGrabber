import pandas as pd
import sys
import datetime
import csv
import GISpy
import TweetMatch
import datetime
import json

#from GISpy import sanitizeTweet, outTime, zipData
from copy import deepcopy
#from os import remove
from dateutil import parser

indexKeys = ['text','created_at']
updateKeys = ['place','nltkCat','tweetType','geoType','lat','lon']
blockKeys = ['$!','$?','$...','#yesallwomen']




def makeKey(tweet,keyList):
    return ','.join([(entry+':'+str(tweet[entry])) for entry in keyList if entry in tweet.keys()])
    
    
    
    
def loadTweets(fileRef,cfg):
    loaded = pd.DataFrame.from_csv(fileRef,index_col='created_at')
    loaded = loaded.reset_index()
    indexed = dict()
    for pos in loaded.index:
        entry = dict(loaded.irow(pos))
        if cfg['Sanitize']:
            entry = GISpy.sanitizeTweet(entry,cfg)
        indexed[makeKey(entry,indexKeys)] = entry
    return indexed
    
    
    
    
def addExtra(data,extraArgs):
    for key in data.keys():
        data[key].update(deepcopy(extraArgs))
        
        
        
        
def getWordWeights(data,daysPast,directory, timeStamp):
    dates = [entry['created_at'] for entry in data.values()]
    rightBound = max(dates)
    leftBound = rightBound - datetime.timedelta(days = daysPast)
    data = [entry for entry in data.values() if leftBound < entry['created_at'] < rightBound]
    
    if  'nlpCat' in data[0].keys():
        CatCol = 'nlpCat'
    elif 'nltkCat' in data[0].keys():
        CatCol = 'nltkCat'
    else:
        CatCol = 'tweetType'
        
    wordWeights = dict()
    wordList = dict()
    wordCloud = []
    wordList['all'] = [TweetMatch.prepTweet(entry['text']) for entry in data] 

    cats = set([entry[CatCol] for entry in data])
    for cat in cats:
        wordList[cat] = [TweetMatch.prepTweet(entry['text']) for entry in data if entry[CatCol] == cat] 

    cats.add('all')
    for cat in cats:
        wordList[cat] = [[word.split("'")[0] for word in entry if word not in blockKeys] for entry in wordList[cat]]
    
    
    for cat in cats:
        wordWeights[cat] = dict()  
        for tweet in wordList[cat]:
            for word in tweet:
                if word not in wordWeights[cat].keys():
                    wordWeights[cat][word] = 1
                else:
                    wordWeights[cat][word] += 1
                    
    for cat in cats:
        listed = []
        for key in wordWeights[cat].keys():
            listed.append('{text: "%s", weight: %s}' % (str(key),wordWeights[cat][key]))
        wordCloud.append('{%s: [%s]}' % (cat,', '.join(listed)))
    
    jsonOut = '{wordcloud: [%s]}' % ', '.join(wordCloud)
    outName = "wordcloud.json"
    print "Writing wordcloud to '"+outName + "'"
    
    outFile = open(directory+outName, "w")
    outFile.write(jsonOut)
    outFile.close()
    return directory+outName

            


def writeCSV(data, directory,name,timeStamp):
    reindexed = data.values()
    orderedKeys = sorted(reindexed[0].keys())
    outName = name + timeStamp.replace(':','.') + '.csv'
    print "Writing collected tweets to '"+outName + "'"
    
    outFile = open(directory+outName, "w") 
    csvOut = csv.DictWriter(outFile,orderedKeys)
    csvOut.writer.writerow(orderedKeys)
    csvOut.writerows(reindexed)
    outFile.close()
    return directory + outName
    



def getMeta(cfg,directory,timeStamp):
    if '_login_' in cfg.keys():
        if cfg['MultiLogin']:
            login = str(cfg['_login_'].keys())
        else:
            login = cfg['_login_']['name']
    else:
        login = cfg['Logins']
    login = login.replace("'",'')
    meta = "{\n\tdate_created: '%s',\n\ttwitter_accounts: '%s',\n\tanalytics: {" % (timeStamp,login)
    meta += "\n\t\twordcloud: {\n\t\t\tstore: {\n\t\t\t\turl: 'wordcloud.json',\n\t\t\t\ttype: 'file'"
    meta += "\n\t\t\t}\n\t\t}\n\t}\n}"
    outFile = open(directory+"metadata.json", "w")
    outFile.write(meta)
    outFile.close()
    return directory+"metadata.json"
    
    


def getDeltas(fileOld, fileNew, cfg, directory):
    loadedNew = loadTweets(fileNew,cfg)
    timeList = [entry['created_at'] for entry in loadedNew.values()]
    minTime = min(timeList)
    
    if not cfg['OneTimeDump']:
        loadedOld = {key:item for key, item in loadTweets(fileOld,cfg).iteritems() if item['created_at'] >= minTime}
    else:
        loadedOld = dict()
    
    merged = deepcopy(loadedOld); merged.update(loadedNew)
    
    newKeys = set(loadedNew.keys())
    oldKeys = set(loadedOld.keys())
    
    addedKeys = newKeys.difference(oldKeys)
    removedKeys = oldKeys.difference(newKeys)
    sameKeys = newKeys.intersection(oldKeys)
    updatedKeys = set([entry for entry in sameKeys if makeKey(loadedNew[entry],updateKeys) != makeKey(loadedOld[entry],updateKeys)])
    expDir = 'studies/'+ cfg['OutDir'] + cfg['Method'] + '/'
    
    timeStamp =  GISpy.outTime(datetime.datetime.now())['db']
    wordWeight = getWordWeights(loadedNew,5,expDir,timeStamp)
    meta = getMeta(cfg,expDir,timeStamp)
    fileLocs = [fileNew,wordWeight,meta]
    
    addedLoc = removedLoc = updatedLoc = 'null'
    
    
    
    if len(addedKeys) >= 1:
        if cfg['OneTimeDump']:
            descriptor = 'Dumped'
            operation = 'dump'
        else:
            descriptor = 'Added'
            operation = 'add'
        addedData = {key:value for key,value in merged.iteritems() if key in addedKeys}
        addExtra(addedData,{'operation':operation,'operationTime':timeStamp})
        addedLoc = writeCSV(addedData,expDir,descriptor,'')
        fileLocs.append(addedLoc)
    if len(removedKeys) >= 1:
        removedData = {key:value for key,value in merged.iteritems() if key in removedKeys}
        addExtra(removedData,{'operation':'remove','operationTime':timeStamp})
        removedLoc = writeCSV(removedData,expDir,"Removed",'')
        fileLocs.append(removedLoc)
    if len(updatedKeys) >= 1:
        updatedData = {key:value for key,value in merged.iteritems() if key in updatedKeys}
        addExtra(updatedData,{'operation':'updated','operationTime':timeStamp})
        updatedLoc = writeCSV(updatedData,expDir,"Updated",'')
        fileLocs.append(updatedLoc)
    
    
    GISpy.zipData(fileLocs,'dbFiles/'+directory,'DBFeed ',timeStamp,cfg)
    return {'wordWeight':wordWeight,'meta':meta,'added':addedLoc,'removed':removedLoc,'updated':updatedLoc}

if __name__ == '__main__':
    cfg = {'Sanitize':False,'MultiLogin':False,'_login_':{'name':'deboo'}}

    getDeltas('novaTrainer_CollectedTweetsOld.csv','novaTrainer_CollectedTweets.csv',cfg)
   