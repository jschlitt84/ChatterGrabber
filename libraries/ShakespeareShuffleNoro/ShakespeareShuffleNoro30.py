from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['NLTK_Ready_Tweets.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro30Score.txt"
index = 30
gen = 73

NLPFreqLimit.append(3)
degrees.append(7)
degrees.append(4)
mode = ["max ent"]
SVMNumber = int(3000*6*0.1*0.1)
SVMMode = 'all'
NLPFreqLimit.append(3)
mode = ["naive bayes"]
NLPFreqLimit.append(2)
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.9*0.9)
SVMNumber = int(3000*3*0.5*0.5)
degrees.append(7)
SVMMode = 'number'
SVMNumber = int(3000*4*0.5*0.5)
SVMNumber = int(3000*4*0.8*0.8)
SVMMode = 'all'
NLPFreqLimit.append(4)
degrees.append(3)
NLPFreqLimit.append(2)

outFile = open(fileName,'w')
if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if ["decision tree"] == mode:
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:2]

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




