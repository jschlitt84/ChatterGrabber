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



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme7Score.txt"
index = 7
gen = 0

degrees.append(6)
mode = ["max ent"]
SVMNumber = int(3000*1*0.2*0.2)
SVMMode = 'all'
SVMNumber = int(3000*7*0.99*0.99)
SVMNumber = int(3000*3*0.7*0.7)
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["naive bayes"]
SVMNumber = int(3000*1*0.7*0.7)
SVMMode = 'ratio'
SVMMode = 'number'
SVMMode = 'all'
SVMMode = 'number'
SVMNumber = int(3000*6*0.6*0.6)
degrees.append(4)
SVMNumber = int(3000*6*0.6*0.6)
degrees.append(4)
degrees.append(6)
NLPFreqLimit.append(4)

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




