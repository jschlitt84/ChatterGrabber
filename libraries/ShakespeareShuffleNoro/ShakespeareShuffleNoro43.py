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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro43Score.txt"
index = 43
gen = 62

SVMMode = 'ratio'
mode = ["svm"]
degrees.append(3)
SVMMode = 'number'
mode = ["max ent"]
NLPFreqLimit.append(3)
SVMMode = 'ratio'
mode = ["decision tree"]
degrees.append(2)
degrees.append(1)
mode = ["decision tree"]
SVMNumber = int(3000*4*0.99*0.99)
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*3*0.4*0.4)
SVMMode = 'all'
degrees.append(3)
mode = ["naive bayes"]
degrees.append(4)
mode = ["naive bayes"]
NLPFreqLimit.append(4)

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




