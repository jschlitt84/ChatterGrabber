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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg20Score.txt"
index = 20
gen = 0

mode = ["decision tree"]
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.6*0.6)
NLPFreqLimit.append(2)
SVMMode = 'ratio'
NLPFreqLimit.append(3)
SVMMode = 'all'
SVMMode = 'all'
degrees.append(3)
mode = ["svm"]
NLPFreqLimit.append(3)
mode = ["svm"]
NLPFreqLimit.append(2)
SVMMode = 'number'
mode = ["decision tree"]
SVMMode = 'all'
degrees.append(4)
mode = ["svm"]
NLPFreqLimit.append(1)
SVMMode = 'ratio'

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




