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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc34Score.txt"
index = 34
gen = 0
prefix = ''
mode = ["svm"]
None
SVMNumber = int(3000*4*0.6*0.6)
mode = ["naive bayes"]
mode = ["max ent"]
SVMMode = 'all'
None
None
SVMNumber = int(3000*3*0.2*0.2)
None
mode = ["svm"]
SVMMode = 'number'
None
SVMNumber = int(3000*7*0.3*0.3)
None
mode = ["max ent"]
degrees.append(6)
None
degrees.append(5)
SVMMode = 'all'

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

