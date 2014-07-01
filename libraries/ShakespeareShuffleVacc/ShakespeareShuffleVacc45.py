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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc45Score.txt"
index = 45
gen = 0
prefix = ''
degrees.append(1)
degrees.append(2)
SVMMode = 'number'
degrees.append(3)
SVMMode = 'all'
degrees.append(5)
mode = ["svm"]
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*6*0.1*0.1)
None
None
SVMMode = 'ratio'
None
mode = ["naive bayes"]
None
mode = ["max ent"]
SVMMode = 'all'
None
SVMNumber = int(3000*5*0.4*0.4)
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

