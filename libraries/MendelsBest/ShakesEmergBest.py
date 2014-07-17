clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path
from os import getcwd

parent = clusterDir

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['EmergNLTKScoring.csv']
cores = 4
iterations = 4
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesEmerg/ShakesEmerg182Score.txt"
index = 182
gen = 9

SVMNumber = int(3000*6*0.6*0.6)
mode = ["decision tree"]
degrees.append(6)
NLPFreqLimit.append(3)
SVMNumber = int(3000*7*0.5*0.5)
NLPFreqLimit.append(5)
degrees.append(1)
SVMNumber = int(3000*2*0.1*0.1)
SVMMode = 'number'
degrees.append(1)
SVMNumber = int(3000*4*0.4*0.4)
NLPFreqLimit.append(1)
NLPFreqLimit.append(2)
SVMNumber = int(3000*2*0.2*0.2)
SVMMode = 'ratio'
SVMMode = 'number'
NLPFreqLimit.append(5)
SVMMode = 'number'
mode = ["svm"]
mode = ["svm"]

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

try:
	score = int(optimizeClassifier.main(args,'mendel'))
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




