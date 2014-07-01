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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc21Score.txt"
index = 21
gen = 0
prefix = ''
None
SVMNumber = int(3000*1*0.2*0.2)
SVMNumber = int(3000*1*0.2*0.2)
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.6*0.6)
None
mode = ["decision tree"]
mode = ["svm"]
None
SVMMode = 'number'
mode = ["svm"]
degrees.append(4)
SVMNumber = int(3000*7*0.5*0.5)
mode = ["naive bayes"]
SVMNumber = int(3000*1*0.1*0.1)
mode = ["decision tree"]
None
SVMNumber = int(3000*7*0.2*0.2)
None
degrees.append(4)

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

