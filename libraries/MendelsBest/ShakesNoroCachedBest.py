clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path
from os import getcwd
from KwikECache import *

parent = clusterDir

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier
prefix = ''
files = ['NLTK_Ready_Tweets.csv']
cores = 8
iterations = 8
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0






fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesNoroCached/ShakesNoroCached802Score.txt"
index = 802
gen = 0

mode = ["decision tree"]
NLPFreqLimit.append(2)
SVMMode = 'all'
SVMNumber = int(3000*6*0.4*0.4)
mode = ["svm"]
degrees.append(7)
degrees.append(1)
SVMMode = 'ratio'
NLPFreqLimit.append(5)
NLPFreqLimit.append(5)
degrees.append(7)
SVMMode = 'number'
mode = ["naive bayes"]
degrees.append(4)
degrees.append(7)
degrees.append(6)
degrees.append(3)
NLPFreqLimit.append(4)
degrees.append(3)
NLPFreqLimit.append(4)

outFile = open(fileName,'w')





if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if ["decision tree"] == mode:
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:2]

cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber,
	'NLPFreqLimit':NLPFreqLimit}

args = {'cores':cores,
	'iterations':iterations,
	'sweepRange':sweepRange,
	'degrees':[list(set(degrees))],
	'mode':mode,
	'cfg':cfg,
	'stops':stops,
	'prefix':prefix,
	'files':files,
	'workingDir':clusterDir,
	'cluster':True}

cacheKey = str(args.values)
getScore(args,cacheKey,cache):
cacheRef = fileName.replace(str(index)+'Score','Cache')
cache = updateCache(dict(),cacheRef,0)




try:
	score = getScore(args,cacheKey,cache,"float(optimizeClassifier.main(args,'mendel'))",0)
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




