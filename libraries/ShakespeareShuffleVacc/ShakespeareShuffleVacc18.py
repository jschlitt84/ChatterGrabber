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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc18Score.txt"
index = 18
gen = 0
prefix = ''
None
None
SVMNumber = int(3000*5*0.3*0.3)
SVMNumber = int(3000*6*0.7*0.7)
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.7*0.7)
SVMMode = 'ratio'
mode = ["decision tree"]
mode = ["decision tree"]
None
SVMMode = 'number'
None
mode = ["decision tree"]
SVMNumber = int(3000*1*0.5*0.5)
SVMMode = 'all'
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'ratio'
degrees.append(7)

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

