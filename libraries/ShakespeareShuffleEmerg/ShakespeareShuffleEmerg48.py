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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg48Score.txt"
index = 48
gen = 0

mode = ["max ent"]
mode = ["max ent"]
mode = ["decision tree"]
SVMNumber = int(3000*7*0.1*0.1)
SVMMode = 'all'
SVMMode = 'all'
SVMMode = 'number'
mode = ["decision tree"]
SVMMode = 'all'
mode = ["svm"]
degrees.append(1)
NLPFreqLimit.append(4)
SVMMode = 'number'
SVMMode = 'all'
SVMMode = 'all'
mode = ["svm"]
SVMNumber = int(3000*7*0.7*0.7)
degrees.append(3)
SVMMode = 'ratio'
degrees.append(7)

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




