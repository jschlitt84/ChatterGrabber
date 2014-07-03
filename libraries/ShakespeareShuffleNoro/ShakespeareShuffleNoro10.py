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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro10Score.txt"
index = 10
gen = 21

SVMMode = 'number'
degrees.append(1)
NLPFreqLimit.append(2)
NLPFreqLimit.append(2)
NLPFreqLimit.append(4)
NLPFreqLimit.append(2)
degrees.append(5)
SVMNumber = int(3000*5*0.9*0.9)
mode = ["decision tree"]
degrees.append(5)
mode = ["naive bayes"]
NLPFreqLimit.append(2)
SVMMode = 'ratio'
mode = ["svm"]
degrees.append(7)
NLPFreqLimit.append(3)
degrees.append(2)
SVMMode = 'number'
degrees.append(7)
SVMNumber = int(3000*2*0.99*0.99)

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




