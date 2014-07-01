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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc46Score.txt"
index = 46
gen = 0
prefix = ''
SVMMode = 'all'
SVMNumber = int(3000*7*0.3*0.3)
degrees.append(3)
mode = ["naive bayes"]
degrees.append(4)
SVMNumber = int(3000*3*0.3*0.3)
mode = ["decision tree"]
SVMNumber = int(3000*2*0.9*0.9)
degrees.append(4)
mode = ["decision tree"]
SVMMode = 'all'
None
mode = ["decision tree"]
None
SVMNumber = int(3000*5*0.9*0.9)
SVMMode = 'all'
SVMMode = 'ratio'
None
mode = ["max ent"]
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

