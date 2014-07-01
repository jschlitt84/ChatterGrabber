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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro26Score.txt"
index = 26
gen = 0
prefix = ''
degrees.append(7)
mode = ["svm"]
degrees.append(5)
None
None
degrees.append(1)
None
SVMMode = 'ratio'
mode = ["decision tree"]
SVMNumber = int(3000*6*0.9*0.9)
None
SVMMode = 'ratio'
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.9*0.9)
degrees.append(2)
mode = ["svm"]
degrees.append(7)
SVMNumber = int(3000*3*0.8*0.8)
SVMMode = 'ratio'
None

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

