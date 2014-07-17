clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path

parent = clusterDir

if parent not in path:
	path.insert(0, parent)

import optimizeClassifier

prefix = ''
files = ['vaccAutNLPScores.csv']
cores = 8
iterations = 8
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0






fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesVaccC/ShakesVaccC317Score.txt"
index = 317
gen = 0

SVMNumber = int(3000*3*0.2*0.2)
degrees.append(7)
SVMMode = 'all'
degrees.append(1)
NLPFreqLimit.append(3)
degrees.append(5)
SVMMode = 'all'
degrees.append(7)
SVMMode = 'number'
mode = ["max ent"]
degrees.append(4)
mode = ["decision tree"]
NLPFreqLimit.append(5)
mode = ["decision tree"]
mode = ["max ent"]
NLPFreqLimit.append(5)
NLPFreqLimit.append(2)
mode = ["svm"]
degrees.append(1)
SVMMode = 'number'

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


score = float(optimizeClassifier.main(args,'mendel'))





