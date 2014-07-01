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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc23Score.txt"
index = 23
gen = 0
prefix = ''
None
SVMNumber = int(3000*4*0.9*0.9)
mode = ["svm"]
None
mode = ["svm"]
mode = ["max ent"]
SVMMode = 'number'
mode = ["svm"]
SVMMode = 'ratio'
SVMMode = 'all'
degrees.append(7)
SVMMode = 'all'
None
None
None
degrees.append(7)
SVMMode = 'ratio'
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.99*0.99)
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

