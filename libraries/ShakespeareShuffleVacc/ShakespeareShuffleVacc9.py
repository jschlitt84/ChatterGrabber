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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc9Score.txt"
index = 9
gen = 0
prefix = ''
SVMNumber = int(3000*5*0.5*0.5)
mode = ["svm"]
degrees.append(6)
degrees.append(7)
degrees.append(3)
mode = ["max ent"]
mode = ["svm"]
mode = ["max ent"]
degrees.append(3)
None
mode = ["decision tree"]
degrees.append(1)
SVMMode = 'ratio'
None
SVMMode = 'ratio'
SVMMode = 'all'
mode = ["svm"]
None
None
SVMNumber = int(3000*6*0.5*0.5)

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

