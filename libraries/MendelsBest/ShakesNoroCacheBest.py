clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path

parent = clusterDir

if parent not in path:
	path.insert(0, parent)

import optimizeClassifier
from KwikECache import *


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






fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesNoroCache/ShakesNoroCache3Score.txt"
index = 3
gen = 0

mode = ["svm"]
degrees.append(5)
SVMNumber = int(3000*1*0.1*0.1)
mode = ["decision tree"]
SVMMode = 'number'
mode = ["decision tree"]
SVMNumber = int(3000*3*0.3*0.3)
SVMNumber = int(3000*2*0.2*0.2)
mode = ["decision tree"]
mode = ["naive bayes"]
SVMMode = 'all'
mode = ["decision tree"]
degrees.append(5)
SVMMode = 'all'
mode = ["svm"]
mode = ["max ent"]
mode = ["svm"]
NLPFreqLimit.append(3)
SVMNumber = int(3000*7*0.6*0.6)
NLPFreqLimit.append(2)

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
cacheRef = fileName.replace(str(index)+'Score','Cache')
cache = updateCache(dict(),cacheRef,0)




try:
	score = getScore(args,cacheKey,cache,"float(optimizeClassifier.main(args,'mendel'))",0)
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




