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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg1Score.txt"
index = 1
gen = 0

degrees.append(4)
mode = ["decision tree"]
SVMNumber = int(3000*1*0.8*0.8)
NLPFreqLimit.append(4)
mode = ["svm"]
NLPFreqLimit.append(3)
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["naive bayes"]
mode = ["svm"]
degrees.append(4)
mode = ["decision tree"]
degrees.append(3)
degrees.append(7)
degrees.append(5)
degrees.append(2)
degrees.append(3)
SVMMode = 'ratio'
mode = ["naive bayes"]
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




