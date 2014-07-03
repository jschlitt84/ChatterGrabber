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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro12Score.txt"
index = 12
gen = 73

degrees.append(3)
degrees.append(1)
SVMMode = 'all'
SVMMode = 'ratio'
SVMMode = 'ratio'
mode = ["svm"]
degrees.append(6)
SVMNumber = int(3000*5*0.1*0.1)
mode = ["svm"]
degrees.append(1)
degrees.append(5)
SVMNumber = int(3000*5*0.9*0.9)
mode = ["decision tree"]
mode = ["svm"]
mode = ["svm"]
SVMMode = 'all'
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.2*0.2)
NLPFreqLimit.append(2)
mode = ["max ent"]

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




