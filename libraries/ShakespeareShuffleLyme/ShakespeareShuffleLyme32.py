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



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme32Score.txt"
index = 32
gen = 0

NLPFreqLimit.append(2)
SVMMode = 'ratio'
degrees.append(1)
SVMMode = 'number'
SVMMode = 'all'
degrees.append(3)
SVMMode = 'ratio'
NLPFreqLimit.append(4)
mode = ["max ent"]
SVMNumber = int(3000*6*0.9*0.9)
mode = ["decision tree"]
SVMMode = 'ratio'
mode = ["max ent"]
SVMMode = 'number'
degrees.append(2)
SVMNumber = int(3000*5*0.4*0.4)
mode = ["decision tree"]
SVMMode = 'number'
mode = ["svm"]
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




