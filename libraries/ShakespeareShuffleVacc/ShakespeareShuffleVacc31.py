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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc31Score.txt"
index = 31
gen = 0
prefix = ''
None
mode = ["max ent"]
SVMMode = 'ratio'
degrees.append(1)
SVMNumber = int(3000*5*0.1*0.1)
SVMNumber = int(3000*4*0.8*0.8)
None
degrees.append(7)
mode = ["decision tree"]
mode = ["svm"]
SVMMode = 'number'
degrees.append(4)
SVMMode = 'ratio'
degrees.append(5)
degrees.append(1)
degrees.append(7)
SVMMode = 'ratio'
None
mode = ["decision tree"]
degrees.append(5)

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

