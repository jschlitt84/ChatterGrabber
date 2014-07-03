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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg6Score.txt"
index = 6
gen = 0

SVMMode = 'number'
SVMNumber = int(3000*1*0.5*0.5)
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(2)
degrees.append(4)
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.99*0.99)
SVMNumber = int(3000*7*0.2*0.2)
SVMMode = 'ratio'
degrees.append(7)
degrees.append(2)
degrees.append(5)
SVMMode = 'all'
degrees.append(3)
SVMMode = 'number'
SVMNumber = int(3000*2*0.3*0.3)
SVMMode = 'all'
SVMNumber = int(3000*4*0.9*0.9)

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




