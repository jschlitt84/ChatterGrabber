import dbm
from TweetMatch import stripUnicode 
import cPickle
import os
import json

cacheRef = '/'.join(os.getcwd().split('/')[0:-1])+'/caches/'
fileRef = cacheRef+'GeoPickle.txt'
dbRef = cacheRef+'GeoPickleDBM'
fileIn = open(fileRef)
geo = cPickle.load(fileIn)
db = dbm.open(dbRef,'n')

for key,item in geo.iteritems():
    db[stripUnicode(key)] = json.dumps(item)