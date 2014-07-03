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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg8Score.txt"
index = 8
gen = 0

NLPFreqLimit.append(4)
degrees.append(1)
SVMNumber = int(3000*3*0.5*0.5)
NLPFreqLimit.append(4)
SVMNumber = int(3000*3*0.1*0.1)
mode = ["naive bayes"]
NLPFreqLimit.append(4)
NLPFreqLimit.append(1)
SVMNumber = int(3000*5*0.7*0.7)
degrees.append(5)
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.5*0.5)
NLPFreqLimit.append(2)
degrees.append(7)
mode = ["naive bayes"]
mode = ["naive bayes"]
degrees.append(7)
NLPFreqLimit.append(2)

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




