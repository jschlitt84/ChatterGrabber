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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg24Score.txt"
index = 24
gen = 0

SVMNumber = int(3000*5*0.8*0.8)
NLPFreqLimit.append(4)
degrees.append(5)
SVMMode = 'ratio'
degrees.append(3)
SVMMode = 'all'
mode = ["decision tree"]
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(3000*1*0.9*0.9)
SVMMode = 'number'
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.5*0.5)
degrees.append(7)
NLPFreqLimit.append(4)
mode = ["naive bayes"]
degrees.append(4)
NLPFreqLimit.append(3)
degrees.append(4)
degrees.append(3)

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




