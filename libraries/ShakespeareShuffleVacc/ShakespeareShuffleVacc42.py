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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc42Score.txt"
index = 42
gen = 0
prefix = ''
None
mode = ["naive bayes"]
mode = ["decision tree"]
degrees.append(7)
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.2*0.2)
SVMNumber = int(3000*1*0.99*0.99)
SVMMode = 'number'
degrees.append(6)
None
None
mode = ["max ent"]
degrees.append(5)
SVMMode = 'number'
SVMMode = 'all'
SVMMode = 'all'
degrees.append(2)
mode = ["svm"]
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(2)

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

