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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc4Score.txt"
index = 4
gen = 0
prefix = ''
mode = ["max ent"]
None
degrees.append(7)
None
None
degrees.append(4)
SVMMode = 'all'
None
mode = ["naive bayes"]
None
SVMNumber = int(3000*1*0.8*0.8)
None
None
None
SVMNumber = int(3000*1*0.2*0.2)
None
None
SVMNumber = int(3000*3*0.4*0.4)
SVMMode = 'all'
mode = ["decision tree"]

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

