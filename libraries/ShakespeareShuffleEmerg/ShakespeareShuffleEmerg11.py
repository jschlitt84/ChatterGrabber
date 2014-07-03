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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg11Score.txt"
index = 11
gen = 0

SVMNumber = int(3000*6*0.6*0.6)
SVMMode = 'number'
degrees.append(6)
SVMMode = 'number'
SVMMode = 'number'
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(4)
SVMMode = 'ratio'
degrees.append(6)
degrees.append(5)
SVMMode = 'ratio'
NLPFreqLimit.append(4)
SVMMode = 'ratio'
degrees.append(2)
SVMMode = 'number'
degrees.append(3)
SVMNumber = int(3000*7*0.6*0.6)
SVMNumber = int(3000*4*0.5*0.5)
mode = ["max ent"]

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




