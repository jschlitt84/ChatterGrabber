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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro32Score.txt"
index = 32
gen = 0
prefix = ''
SVMMode = 'number'
None
degrees.append(2)
None
SVMNumber = int(3000*6*0.9*0.9)
degrees.append(4)
degrees.append(5)
degrees.append(5)
SVMMode = 'all'
None
None
degrees.append(1)
SVMNumber = int(3000*7*0.1*0.1)
SVMNumber = int(3000*2*0.8*0.8)
mode = ["svm"]
mode = ["svm"]
None
None
mode = ["svm"]
SVMNumber = int(3000*4*0.7*0.7)

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

