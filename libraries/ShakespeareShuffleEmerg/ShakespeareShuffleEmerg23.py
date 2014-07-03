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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg23Score.txt"
index = 23
gen = 0

NLPFreqLimit.append(1)
NLPFreqLimit.append(1)
SVMNumber = int(3000*3*0.8*0.8)
degrees.append(6)
mode = ["max ent"]
SVMNumber = int(3000*5*0.4*0.4)
SVMNumber = int(3000*3*0.1*0.1)
NLPFreqLimit.append(3)
SVMNumber = int(3000*5*0.7*0.7)
SVMMode = 'all'
degrees.append(6)
degrees.append(5)
SVMNumber = int(3000*6*0.6*0.6)
degrees.append(7)
NLPFreqLimit.append(2)
mode = ["max ent"]
NLPFreqLimit.append(4)
mode = ["svm"]
mode = ["naive bayes"]
degrees.append(4)

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




