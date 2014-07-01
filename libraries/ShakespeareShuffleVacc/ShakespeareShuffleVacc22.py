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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc22Score.txt"
index = 22
gen = 0
prefix = ''
SVMMode = 'number'
mode = ["max ent"]
mode = ["naive bayes"]
mode = ["max ent"]
degrees.append(3)
mode = ["decision tree"]
None
degrees.append(7)
mode = ["max ent"]
None
SVMNumber = int(3000*4*0.7*0.7)
SVMNumber = int(3000*1*0.8*0.8)
degrees.append(5)
None
SVMNumber = int(3000*2*0.6*0.6)
SVMNumber = int(3000*6*0.3*0.3)
mode = ["decision tree"]
None
mode = ["decision tree"]
mode = ["svm"]

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

