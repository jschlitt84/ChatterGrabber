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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro16Score.txt"
index = 16
gen = 70

NLPFreqLimit.append(4)
NLPFreqLimit.append(3)
degrees.append(2)
NLPFreqLimit.append(1)
mode = ["svm"]
mode = ["svm"]
SVMMode = 'ratio'
SVMMode = 'number'
degrees.append(1)
degrees.append(6)
SVMNumber = int(3000*4*0.4*0.4)
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.99*0.99)
NLPFreqLimit.append(4)
degrees.append(3)
NLPFreqLimit.append(3)
mode = ["svm"]
SVMNumber = int(3000*7*0.3*0.3)
NLPFreqLimit.append(1)
SVMMode = 'number'

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




