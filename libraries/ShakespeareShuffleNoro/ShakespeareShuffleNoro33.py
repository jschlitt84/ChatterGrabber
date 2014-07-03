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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro33Score.txt"
index = 33
gen = 0

mode = ["decision tree"]
mode = ["decision tree"]
NLPFreqLimit.append(2)
NLPFreqLimit.append(2)
NLPFreqLimit.append(4)
degrees.append(3)
degrees.append(3)
degrees.append(1)
SVMNumber = int(3000*5*0.7*0.7)
degrees.append(6)
NLPFreqLimit.append(3)
SVMNumber = int(3000*2*0.1*0.1)
mode = ["decision tree"]
mode = ["svm"]
degrees.append(7)
mode = ["naive bayes"]
degrees.append(2)
NLPFreqLimit.append(2)
NLPFreqLimit.append(4)
degrees.append(3)

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




