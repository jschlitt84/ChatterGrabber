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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc44Score.txt"
index = 44
gen = 0
prefix = ''
None
degrees.append(3)
None
mode = ["svm"]
degrees.append(2)
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.8*0.8)
degrees.append(5)
SVMMode = 'all'
SVMMode = 'all'
mode = ["max ent"]
None
degrees.append(3)
None
None
degrees.append(1)
mode = ["naive bayes"]
None
mode = ["max ent"]
SVMNumber = int(3000*3*0.99*0.99)

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

