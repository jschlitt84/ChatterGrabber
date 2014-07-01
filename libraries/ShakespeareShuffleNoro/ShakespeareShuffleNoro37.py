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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro37Score.txt"
index = 37
gen = 0
prefix = ''
SVMMode = 'ratio'
mode = ["svm"]
SVMMode = 'ratio'
SVMMode = 'number'
mode = ["decision tree"]
SVMMode = 'all'
None
None
degrees.append(2)
None
degrees.append(5)
None
SVMNumber = int(3000*4*0.9*0.9)
SVMNumber = int(3000*3*0.2*0.2)
mode = ["decision tree"]
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.8*0.8)
None
mode = ["svm"]
SVMNumber = int(3000*6*0.1*0.1)

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

