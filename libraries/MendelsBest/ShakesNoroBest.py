clusterDir = "/home/NDSSL/study/ChatterGrabber/libraries/"
from sys import path
from os import getcwd

parent = clusterDir

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['NLTK_Ready_Tweets.csv']
cores = 4
iterations = 4
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "/home/NDSSL/study/ChatterGrabber/libraries/ShakesNoro/ShakesNoro223Score.txt"
index = 223
gen = 51

NLPFreqLimit.append(1)
NLPFreqLimit.append(1)
SVMMode = 'all'
SVMMode = 'all'
degrees.append(5)
SVMNumber = int(3000*7*0.4*0.4)
NLPFreqLimit.append(5)
SVMNumber = int(3000*2*0.5*0.5)
SVMMode = 'all'
mode = ["max ent"]
degrees.append(4)
SVMMode = 'number'
mode = ["svm"]
degrees.append(1)
degrees.append(7)
SVMMode = 'number'
degrees.append(1)
NLPFreqLimit.append(5)
SVMMode = 'all'
SVMMode = 'number'

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




