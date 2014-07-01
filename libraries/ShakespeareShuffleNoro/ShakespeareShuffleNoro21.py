from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['NLTK_Ready_Tweets.csv']
cores = 2
iterations = 3
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro21Score.txt"
index = 21
gen = 0
prefix = ''
mode = ["decision tree"]
SVMNumber = int(3000*7*0.8*0.8)
SVMNumber = int(3000*3*0.4*0.4)
None
mode = ["naive bayes"]
degrees.append(1)
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.7*0.7)
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*6*0.9*0.9)
degrees.append(5)
degrees.append(3)
None
None
None
degrees.append(1)
SVMMode = 'all'
mode = ["naive bayes"]

outFile = open(fileName,'w')
cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber}
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

