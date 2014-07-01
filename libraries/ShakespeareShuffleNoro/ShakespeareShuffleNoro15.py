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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro15Score.txt"
index = 15
gen = 0
prefix = ''
mode = ["decision tree"]
SVMNumber = int(3000*1*0.1*0.1)
mode = ["decision tree"]
degrees.append(5)
SVMNumber = int(3000*4*0.6*0.6)
degrees.append(3)
mode = ["svm"]
SVMMode = 'all'
degrees.append(2)
SVMMode = 'number'
degrees.append(2)
mode = ["max ent"]
None
degrees.append(2)
mode = ["decision tree"]
SVMMode = 'ratio'
degrees.append(4)
SVMMode = 'all'
degrees.append(3)
degrees.append(6)

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

