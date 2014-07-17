clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path

parent = clusterDir

if parent not in path:
	path.insert(0, parent)

import optimizeClassifier
from KwikECache import *


prefix = ''
files = ['EmergNLTKScoring.csv']
cores = 8
iterations = 8
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0






fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesEmergC/ShakesEmergC266Score.txt"
index = 266
gen = 5

NLPFreqLimit.append(5)
NLPFreqLimit.append(5)
SVMMode = 'number'
NLPFreqLimit.append(5)
mode = ["svm"]
mode = ["naive bayes"]
NLPFreqLimit.append(4)
degrees.append(2)
mode = ["max ent"]
SVMNumber = int(3000*2*0.4*0.4)
SVMMode = 'number'
NLPFreqLimit.append(5)
NLPFreqLimit.append(2)
NLPFreqLimit.append(3)
NLPFreqLimit.append(4)
NLPFreqLimit.append(4)
degrees.append(1)
mode = ["naive bayes"]
degrees.append(7)
SVMNumber = int(3000*6*0.99*0.99)

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
	cfg = {'SVMMode':SVMMode,'SVMOrder':'GVTMACFSN',
		'SVMNumber':SVMNumber,
		'NLPFreqLimit':NLPFreqLimit}
else:
        cfg = {'SVMMode':'All','SVMOrder':'GVTMACFSN',
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



score = int(optimizeClassifier.main(args,'mendel'))



