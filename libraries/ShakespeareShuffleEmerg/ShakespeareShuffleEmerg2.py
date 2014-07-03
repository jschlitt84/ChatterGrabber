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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg2Score.txt"
index = 2
gen = 0

mode = ["decision tree"]
mode = ["decision tree"]
SVMMode = 'all'
SVMMode = 'ratio'
degrees.append(6)
SVMNumber = int(3000*7*0.4*0.4)
NLPFreqLimit.append(3)
mode = ["naive bayes"]
degrees.append(1)
NLPFreqLimit.append(1)
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(7)
degrees.append(6)
SVMMode = 'all'
mode = ["svm"]
SVMMode = 'ratio'
SVMMode = 'number'
NLPFreqLimit.append(4)
NLPFreqLimit.append(1)
SVMNumber = int(3000*2*0.99*0.99)

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




