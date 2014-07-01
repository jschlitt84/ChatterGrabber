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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro33Score.txt"
index = 33
gen = 0
prefix = ''
None
None
SVMMode = 'number'
mode = ["svm"]
SVMMode = 'ratio'
None
SVMNumber = int(3000*4*0.6*0.6)
SVMNumber = int(3000*6*0.9*0.9)
degrees.append(5)
SVMMode = 'all'
None
SVMMode = 'ratio'
None
SVMMode = 'ratio'
mode = ["decision tree"]
SVMMode = 'ratio'
degrees.append(5)
SVMNumber = int(3000*7*0.5*0.5)
degrees.append(7)
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

