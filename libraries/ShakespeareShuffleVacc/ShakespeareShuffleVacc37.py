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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc37Score.txt"
index = 37
gen = 0
prefix = ''
SVMMode = 'number'
SVMMode = 'number'
mode = ["naive bayes"]
None
SVMNumber = int(3000*7*0.9*0.9)
None
degrees.append(3)
degrees.append(6)
SVMNumber = int(3000*4*0.4*0.4)
None
None
None
SVMNumber = int(3000*2*0.3*0.3)
degrees.append(5)
degrees.append(3)
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(4)
degrees.append(6)
SVMNumber = int(3000*4*0.9*0.9)

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

