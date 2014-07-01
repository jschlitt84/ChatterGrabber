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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro31Score.txt"
index = 31
gen = 0
prefix = ''
SVMMode = 'all'
SVMNumber = int(3000*1*0.8*0.8)
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.1*0.1)
SVMNumber = int(3000*1*0.7*0.7)
SVMMode = 'number'
SVMMode = 'ratio'
None
SVMMode = 'number'
SVMMode = 'ratio'
None
SVMMode = 'number'
degrees.append(1)
mode = ["svm"]
degrees.append(2)
SVMNumber = int(3000*5*0.6*0.6)
None
SVMMode = 'number'
SVMNumber = int(3000*6*0.5*0.5)
mode = ["decision tree"]

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

