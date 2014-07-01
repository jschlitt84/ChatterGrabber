from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['vaccAutNLPScores.csv']
cores = 2
iterations = 3
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc8Score.txt"
index = 8
gen = 0
prefix = ''
mode = ["max ent"]
mode = ["decision tree"]
degrees.append(2)
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.9*0.9)
mode = ["svm"]
mode = ["max ent"]
mode = ["max ent"]
degrees.append(1)
SVMMode = 'ratio'
None
SVMNumber = int(3000*6*0.7*0.7)
SVMNumber = int(3000*6*0.7*0.7)
mode = ["naive bayes"]
mode = ["decision tree"]
mode = ["decision tree"]
mode = ["decision tree"]
mode = ["svm"]
None
SVMMode = 'all'

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

