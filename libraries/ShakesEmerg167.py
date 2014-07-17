clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path
from os import getcwd

parent = clusterDir

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['EmergNLTKScoring.csv']
cores = 5
iterations = 5
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesEmerg/ShakesEmerg167Score.txt"
index = 167
gen = 15

degrees.append(5)
SVMNumber = int(3000*4*0.5*0.5)
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.5*0.5)
SVMNumber = int(3000*4*0.5*0.5)
SVMMode = 'ratio'
NLPFreqLimit.append(4)
NLPFreqLimit.append(2)
SVMNumber = int(3000*7*0.8*0.8)
degrees.append(6)
degrees.append(4)
NLPFreqLimit.append(3)
NLPFreqLimit.append(3)
degrees.append(1)
SVMNumber = int(3000*2*0.1*0.1)
NLPFreqLimit.append(3)
SVMNumber = int(3000*2*0.7*0.7)
SVMNumber = int(3000*7*0.7*0.7)
SVMMode = 'all'
SVMMode = 'all'

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
	score = float(optimizeClassifier.main(args,'mendel'))
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




