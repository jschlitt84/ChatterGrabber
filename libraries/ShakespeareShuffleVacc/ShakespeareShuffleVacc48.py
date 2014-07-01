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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc48Score.txt"
index = 48
gen = 0
prefix = ''
mode = ["svm"]
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(1)
None
degrees.append(6)
mode = ["max ent"]
SVMMode = 'all'
degrees.append(6)
SVMMode = 'all'
SVMMode = 'all'
mode = ["decision tree"]
degrees.append(2)
SVMMode = 'number'
SVMMode = 'ratio'
SVMNumber = int(3000*2*0.7*0.7)
degrees.append(7)
SVMMode = 'ratio'
SVMNumber = int(3000*2*0.4*0.4)
mode = ["max ent"]

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

