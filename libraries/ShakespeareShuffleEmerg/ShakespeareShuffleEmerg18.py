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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg18Score.txt"
index = 18
gen = 0

SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(1)
NLPFreqLimit.append(1)
degrees.append(5)
NLPFreqLimit.append(2)
SVMMode = 'number'
mode = ["svm"]
mode = ["naive bayes"]
NLPFreqLimit.append(4)
SVMNumber = int(3000*7*0.1*0.1)
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["max ent"]
mode = ["svm"]
SVMMode = 'number'
SVMMode = 'all'
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'all'

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




