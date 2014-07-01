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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc13Score.txt"
index = 13
gen = 0
prefix = ''
None
SVMMode = 'number'
mode = ["svm"]
degrees.append(1)
None
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.2*0.2)
SVMNumber = int(3000*5*0.9*0.9)
degrees.append(2)
mode = ["svm"]
None
None
SVMNumber = int(3000*5*0.2*0.2)
None
SVMMode = 'ratio'
degrees.append(1)
degrees.append(7)
SVMNumber = int(3000*7*0.3*0.3)
None
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

