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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg31Score.txt"
index = 31
gen = 0

NLPFreqLimit.append(1)
NLPFreqLimit.append(2)
mode = ["decision tree"]
SVMNumber = int(3000*4*0.1*0.1)
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.6*0.6)
NLPFreqLimit.append(4)
SVMNumber = int(3000*5*0.3*0.3)
degrees.append(5)
SVMNumber = int(3000*6*0.1*0.1)
NLPFreqLimit.append(4)
mode = ["decision tree"]
mode = ["naive bayes"]
SVMMode = 'all'
SVMMode = 'number'
SVMMode = 'all'
SVMNumber = int(3000*3*0.2*0.2)
SVMMode = 'all'
SVMNumber = int(3000*3*0.4*0.4)
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




