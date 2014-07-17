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






fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesNoroC/ShakesNoroC166Score.txt"
index = 166
gen = 80

mode = ["svm"]
mode = ["max ent"]
NLPFreqLimit.append(1)
degrees.append(1)
SVMNumber = int(3000*3*0.2*0.2)
degrees.append(7)
SVMMode = 'all'
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*2*0.7*0.7)
degrees.append(6)
NLPFreqLimit.append(4)
SVMNumber = int(3000*5*0.2*0.2)
NLPFreqLimit.append(4)
NLPFreqLimit.append(3)
NLPFreqLimit.append(4)
mode = ["svm"]
SVMNumber = int(3000*7*0.3*0.3)
SVMMode = 'all'
degrees.append(2)
SVMNumber = int(3000*7*0.99*0.99)

outFile = open(fileName,'w')


NLPFreqLimit = NLPFreqLimit[:len(degrees)]


if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if ["decision tree"] == mode:
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:2]

if ["svm"] == mode:
	cfg = {'SVMMode':SVMMode,
		'SVMNumber':SVMNumber,
		'NLPFreqLimit':NLPFreqLimit}
else:
        cfg = {'SVMMode':'All',
                'SVMNumber':0,
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



cache  = dict()
cacheKey = str(args.values())
cacheRef = fileName.replace(str(index)+'Score','Cache')
updateCache(cache,cacheRef,0)

if True:
	score = getNLPScore(cacheKey,cache,cacheRef,args,0)
	outFile.write(str(score))
else:
	outFile.write('0')

outFile.close()




