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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc17Score.txt"
index = 17
gen = 0
prefix = ''
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.6*0.6)
None
SVMMode = 'ratio'
mode = ["max ent"]
None
SVMMode = 'number'
mode = ["decision tree"]
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.3*0.3)
None
SVMMode = 'ratio'
degrees.append(3)
mode = ["naive bayes"]
mode = ["svm"]
SVMNumber = int(3000*5*0.2*0.2)
SVMNumber = int(3000*4*0.3*0.3)
degrees.append(5)
SVMMode = 'ratio'
degrees.append(6)

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

