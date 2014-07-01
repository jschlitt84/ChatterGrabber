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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc15Score.txt"
index = 15
gen = 0
prefix = ''
mode = ["max ent"]
mode = ["max ent"]
SVMMode = 'ratio'
SVMMode = 'all'
mode = ["max ent"]
degrees.append(5)
mode = ["svm"]
mode = ["max ent"]
degrees.append(2)
SVMMode = 'number'
SVMMode = 'number'
SVMNumber = int(3000*1*0.5*0.5)
degrees.append(7)
mode = ["decision tree"]
None
mode = ["svm"]
degrees.append(6)
mode = ["naive bayes"]
degrees.append(3)
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

