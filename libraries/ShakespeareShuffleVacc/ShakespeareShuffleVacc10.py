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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc10Score.txt"
index = 10
gen = 0
prefix = ''
None
None
None
SVMMode = 'number'
SVMNumber = int(3000*2*0.1*0.1)
None
degrees.append(7)
degrees.append(3)
SVMNumber = int(3000*7*0.3*0.3)
SVMNumber = int(3000*5*0.6*0.6)
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.7*0.7)
SVMNumber = int(3000*3*0.9*0.9)
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMMode = 'all'
degrees.append(4)
SVMMode = 'ratio'
None
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

