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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro7Score.txt"
index = 7
gen = 0
prefix = ''
SVMNumber = int(3000*6*0.9*0.9)
SVMNumber = int(3000*5*0.9*0.9)
None
SVMMode = 'number'
degrees.append(2)
SVMNumber = int(3000*3*0.9*0.9)
SVMMode = 'ratio'
degrees.append(5)
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["svm"]
mode = ["decision tree"]
None
mode = ["max ent"]
None
mode = ["max ent"]
degrees.append(5)
None
degrees.append(7)
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

