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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro12Score.txt"
index = 12
gen = 0
prefix = ''
mode = ["decision tree"]
SVMNumber = int(3000*2*0.9*0.9)
SVMMode = 'number'
SVMNumber = int(3000*4*0.1*0.1)
None
degrees.append(1)
SVMNumber = int(3000*7*0.2*0.2)
mode = ["decision tree"]
SVMMode = 'ratio'
degrees.append(4)
degrees.append(6)
SVMNumber = int(3000*4*0.3*0.3)
None
mode = ["decision tree"]
mode = ["svm"]
SVMMode = 'all'
mode = ["naive bayes"]
degrees.append(6)
SVMMode = 'number'
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

