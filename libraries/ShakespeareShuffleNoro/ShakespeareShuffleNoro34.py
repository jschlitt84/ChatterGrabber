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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro34Score.txt"
index = 34
gen = 64

degrees.append(6)
SVMMode = 'all'
degrees.append(3)
NLPFreqLimit.append(1)
degrees.append(6)
degrees.append(1)
NLPFreqLimit.append(1)
mode = ["svm"]
SVMMode = 'all'
NLPFreqLimit.append(1)
mode = ["naive bayes"]
NLPFreqLimit.append(1)
mode = ["max ent"]
degrees.append(2)
degrees.append(7)
NLPFreqLimit.append(2)
SVMNumber = int(3000*4*0.7*0.7)
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.4*0.4)
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




