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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc19Score.txt"
index = 19
gen = 0
prefix = ''
mode = ["svm"]
mode = ["max ent"]
mode = ["naive bayes"]
SVMMode = 'number'
None
degrees.append(7)
None
SVMMode = 'number'
SVMMode = 'number'
None
degrees.append(3)
mode = ["max ent"]
mode = ["decision tree"]
SVMMode = 'ratio'
None
degrees.append(2)
None
SVMMode = 'all'
SVMNumber = int(3000*5*0.99*0.99)
SVMMode = 'number'

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

