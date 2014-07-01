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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc39Score.txt"
index = 39
gen = 0
prefix = ''
degrees.append(2)
degrees.append(3)
degrees.append(4)
SVMMode = 'all'
SVMMode = 'all'
mode = ["max ent"]
None
mode = ["svm"]
SVMMode = 'all'
SVMMode = 'ratio'
None
SVMMode = 'ratio'
SVMMode = 'number'
degrees.append(7)
SVMNumber = int(3000*5*0.3*0.3)
mode = ["decision tree"]
SVMMode = 'ratio'
degrees.append(3)
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

