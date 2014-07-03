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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro19Score.txt"
index = 19
gen = 30

SVMNumber = int(3000*6*0.1*0.1)
SVMMode = 'number'
mode = ["decision tree"]
mode = ["naive bayes"]
SVMMode = 'all'
NLPFreqLimit.append(3)
degrees.append(1)
mode = ["naive bayes"]
degrees.append(2)
SVMNumber = int(3000*6*0.8*0.8)
mode = ["decision tree"]
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(3000*3*0.3*0.3)
SVMMode = 'all'
NLPFreqLimit.append(1)
SVMMode = 'all'
degrees.append(6)
SVMMode = 'ratio'
mode = ["svm"]

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




