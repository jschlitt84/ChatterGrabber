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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro22Score.txt"
index = 22
gen = 47

SVMNumber = int(3000*3*0.9*0.9)
mode = ["max ent"]
degrees.append(1)
SVMMode = 'number'
NLPFreqLimit.append(1)
mode = ["svm"]
mode = ["svm"]
degrees.append(5)
SVMNumber = int(3000*2*0.1*0.1)
mode = ["decision tree"]
NLPFreqLimit.append(3)
SVMMode = 'ratio'
NLPFreqLimit.append(1)
SVMNumber = int(3000*4*0.4*0.4)
mode = ["decision tree"]
NLPFreqLimit.append(4)
mode = ["max ent"]
SVMMode = 'ratio'
NLPFreqLimit.append(3)
degrees.append(1)

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




