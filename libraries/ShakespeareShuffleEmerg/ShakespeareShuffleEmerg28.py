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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg28Score.txt"
index = 28
gen = 0

SVMNumber = int(3000*1*0.5*0.5)
SVMNumber = int(3000*7*0.5*0.5)
SVMMode = 'ratio'
SVMMode = 'all'
mode = ["decision tree"]
degrees.append(3)
SVMNumber = int(3000*5*0.99*0.99)
SVMNumber = int(3000*3*0.4*0.4)
mode = ["svm"]
SVMMode = 'ratio'
NLPFreqLimit.append(2)
mode = ["max ent"]
SVMNumber = int(3000*6*0.3*0.3)
mode = ["naive bayes"]
mode = ["max ent"]
SVMMode = 'number'
SVMMode = 'number'
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.3*0.3)
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




