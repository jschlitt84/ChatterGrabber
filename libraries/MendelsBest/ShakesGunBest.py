clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path
from os import getcwd

parent = clusterDir

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['GunTrackerNLTK.csv']
cores = 5
iterations = 5
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesGun/ShakesGun177Score.txt"
index = 177
gen = 1

degrees.append(1)
SVMNumber = int(3000*3*0.8*0.8)
mode = ["naive bayes"]
SVMMode = 'number'
NLPFreqLimit.append(4)
degrees.append(2)
SVMMode = 'ratio'
SVMMode = 'ratio'
mode = ["svm"]
degrees.append(7)
NLPFreqLimit.append(2)
NLPFreqLimit.append(3)
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["max ent"]
NLPFreqLimit.append(3)
degrees.append(1)
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.4*0.4)
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

try:
	score = float(optimizeClassifier.main(args,'mendel'))
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




