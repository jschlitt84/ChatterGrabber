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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc16Score.txt"
index = 16
gen = 0
prefix = ''
mode = ["max ent"]
SVMMode = 'number'
mode = ["max ent"]
SVMMode = 'number'
degrees.append(1)
mode = ["svm"]
SVMMode = 'number'
SVMMode = 'ratio'
SVMMode = 'ratio'
None
SVMNumber = int(3000*4*0.9*0.9)
degrees.append(3)
None
SVMMode = 'number'
None
SVMMode = 'number'
None
mode = ["naive bayes"]
degrees.append(4)
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

