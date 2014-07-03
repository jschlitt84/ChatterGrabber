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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg47Score.txt"
index = 47
gen = 0

degrees.append(2)
degrees.append(4)
degrees.append(3)
NLPFreqLimit.append(3)
SVMMode = 'number'
degrees.append(4)
SVMMode = 'ratio'
NLPFreqLimit.append(2)
degrees.append(1)
NLPFreqLimit.append(1)
mode = ["svm"]
NLPFreqLimit.append(4)
mode = ["svm"]
SVMNumber = int(3000*4*0.6*0.6)
SVMNumber = int(3000*5*0.99*0.99)
SVMMode = 'ratio'
degrees.append(4)
SVMNumber = int(3000*3*0.9*0.9)
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.8*0.8)

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




