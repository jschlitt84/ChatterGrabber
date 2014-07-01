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



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme24Score.txt"
index = 24
gen = 0

NLPFreqLimit.append(1)
SVMNumber = int(3000*7*0.99*0.99)
SVMMode = 'number'
SVMMode = 'number'
NLPFreqLimit.append(4)
degrees.append(7)
mode = ["naive bayes"]
SVMMode = 'all'
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.99*0.99)
SVMMode = 'ratio'
mode = ["decision tree"]
SVMNumber = int(3000*1*0.9*0.9)
NLPFreqLimit.append(1)
degrees.append(6)
degrees.append(3)
degrees.append(5)
degrees.append(7)
degrees.append(7)
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




