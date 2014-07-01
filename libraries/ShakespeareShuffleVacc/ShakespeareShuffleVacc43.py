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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc43Score.txt"
index = 43
gen = 0
prefix = ''
None
mode = ["svm"]
SVMMode = 'all'
SVMNumber = int(3000*3*0.99*0.99)
None
SVMMode = 'all'
degrees.append(6)
mode = ["decision tree"]
mode = ["max ent"]
degrees.append(6)
None
SVMMode = 'ratio'
SVMMode = 'all'
mode = ["svm"]
SVMNumber = int(3000*7*0.3*0.3)
degrees.append(2)
SVMMode = 'all'
degrees.append(6)
SVMNumber = int(3000*3*0.7*0.7)
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

