from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['lymeScores.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme35Score.txt"
index = 35
gen = 0

SVMMode = 'all'
mode = ["decision tree"]
SVMNumber = int(3000*5*0.8*0.8)
NLPFreqLimit.append(1)
mode = ["svm"]
NLPFreqLimit.append(3)
SVMNumber = int(3000*1*0.2*0.2)
NLPFreqLimit.append(3)
mode = ["naive bayes"]
mode = ["decision tree"]
SVMNumber = int(3000*1*0.4*0.4)
NLPFreqLimit.append(2)
NLPFreqLimit.append(1)
mode = ["max ent"]
SVMMode = 'all'
SVMNumber = int(3000*5*0.3*0.3)
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.9*0.9)
degrees.append(5)
mode = ["svm"]

outFile = open(fileName,'w')
if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if mode == "decision tree":
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:1]

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
	'files':files}

try:
	score = int(optimizeClassifier.main(args,'mendel'))
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




