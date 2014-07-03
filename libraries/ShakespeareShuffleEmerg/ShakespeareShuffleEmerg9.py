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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg9Score.txt"
index = 9
gen = 0

mode = ["naive bayes"]
SVMMode = 'number'
degrees.append(3)
SVMMode = 'all'
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["naive bayes"]
SVMMode = 'ratio'
NLPFreqLimit.append(3)
SVMNumber = int(3000*3*0.3*0.3)
SVMMode = 'all'
SVMMode = 'all'
SVMMode = 'all'
SVMMode = 'number'
SVMMode = 'all'
SVMNumber = int(3000*2*0.4*0.4)
SVMMode = 'ratio'
degrees.append(3)
SVMNumber = int(3000*7*0.9*0.9)
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




