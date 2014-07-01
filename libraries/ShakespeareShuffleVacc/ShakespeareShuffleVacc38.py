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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc38Score.txt"
index = 38
gen = 0
prefix = ''
mode = ["svm"]
SVMMode = 'ratio'
degrees.append(6)
degrees.append(7)
degrees.append(7)
mode = ["svm"]
mode = ["naive bayes"]
None
SVMNumber = int(3000*5*0.8*0.8)
degrees.append(4)
mode = ["decision tree"]
SVMNumber = int(3000*3*0.8*0.8)
SVMMode = 'number'
SVMNumber = int(3000*3*0.8*0.8)
None
SVMNumber = int(3000*3*0.9*0.9)
None
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.9*0.9)
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

