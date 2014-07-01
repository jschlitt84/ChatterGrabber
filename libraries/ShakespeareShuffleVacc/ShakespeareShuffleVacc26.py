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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc26Score.txt"
index = 26
gen = 0
prefix = ''
None
None
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["naive bayes"]
None
SVMMode = 'number'
SVMNumber = int(3000*4*0.7*0.7)
None
degrees.append(5)
degrees.append(3)
None
None
SVMNumber = int(3000*2*0.9*0.9)
mode = ["max ent"]
SVMMode = 'all'
None
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

