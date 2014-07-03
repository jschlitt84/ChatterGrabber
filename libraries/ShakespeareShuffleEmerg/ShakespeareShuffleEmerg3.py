from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['EmergNLTKScoring.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg3Score.txt"
index = 3
gen = 0

NLPFreqLimit.append(3)
degrees.append(3)
degrees.append(4)
SVMMode = 'all'
SVMMode = 'ratio'
SVMMode = 'ratio'
NLPFreqLimit.append(4)
mode = ["svm"]
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.8*0.8)
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(7)
mode = ["naive bayes"]
SVMMode = 'ratio'
NLPFreqLimit.append(1)
SVMMode = 'number'
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(3000*6*0.9*0.9)
NLPFreqLimit.append(1)

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




