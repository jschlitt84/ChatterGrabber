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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro4Score.txt"
index = 4
gen = 0

SVMMode = 'number'
mode = ["svm"]
SVMMode = 'all'
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.2*0.2)
NLPFreqLimit.append(3)
SVMMode = 'ratio'
degrees.append(5)
SVMMode = 'number'
NLPFreqLimit.append(1)
degrees.append(5)
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.5*0.5)
mode = ["svm"]
degrees.append(1)
NLPFreqLimit.append(3)
mode = ["naive bayes"]
mode = ["naive bayes"]
mode = ["naive bayes"]
NLPFreqLimit.append(3)

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




