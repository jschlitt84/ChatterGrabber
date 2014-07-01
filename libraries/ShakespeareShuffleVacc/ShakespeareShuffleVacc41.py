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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc41Score.txt"
index = 41
gen = 0
prefix = ''
None
SVMNumber = int(3000*4*0.4*0.4)
SVMNumber = int(3000*5*0.4*0.4)
None
None
degrees.append(1)
degrees.append(4)
SVMMode = 'all'
degrees.append(3)
None
None
SVMNumber = int(3000*4*0.7*0.7)
mode = ["svm"]
SVMMode = 'all'
mode = ["svm"]
mode = ["decision tree"]
None
SVMMode = 'all'
SVMMode = 'all'
mode = ["naive bayes"]

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

