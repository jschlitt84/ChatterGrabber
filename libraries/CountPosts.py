import os
import json
from glob import glob

cwd = os.getcwd()
studyDir = '/'.join(cwd.split('/')[:-1])+'/studies/'

print "Opening",studyDir
studyDirs = glob(studyDir+'*/search/')

print studyDirs

ref = '/Users/jamesschlitt/ChatterGrabber/studies/bigGIHunterDemo/search/Raw_bigGIHunter_Wed 30 Jul 2014 22:54:26.json'

def countPosts(ref):
    fileIn = open(ref)
    text = '/n'.join(fileIn.readlines())
    fileIn.close()
    counted = text.count('{\\"contributors\\":')
    #print '\t',counted, ref
    return counted
    
def countTopic(ref):
    inTopic = glob(ref+"Raw*.json")
    counted = 0
    for collection in inTopic:
        counted += countPosts(collection)
    files = sorted(inTopic, key=os.path.getctime)
    oldest = files[0].split('/')[-1]
    newest = files[-1].split('/')[-1]
    print counted, oldest, newest
    
def countAll(listed):
    for entry in listed:
	try:        
		countTopic(entry)
        except:
		None
    
countAll(studyDirs)
