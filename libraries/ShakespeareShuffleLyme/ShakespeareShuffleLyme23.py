from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['lymeScores.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme23Score.txt"
index = 23
gen = 0

mode = ["max ent"]
mode = ["svm"]
SVMMode = 'ratio'
SVMMode = 'ratio'
mode = ["svm"]
mode = ["max ent"]
SVMNumber = int(3000*7*0.2*0.2)
SVMNumber = int(3000*2*0.8*0.8)
mode = ["max ent"]
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["max ent"]
SVMNumber = int(3000*3*0.1*0.1)
NLPFreqLimit.append(4)
degrees.append(5)
degrees.append(1)
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(6)
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




