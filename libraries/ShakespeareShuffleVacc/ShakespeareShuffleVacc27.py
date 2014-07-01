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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc27Score.txt"
index = 27
gen = 0
prefix = ''
SVMMode = 'number'
mode = ["svm"]
SVMNumber = int(3000*4*0.99*0.99)
SVMNumber = int(3000*7*0.8*0.8)
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(3000*3*0.1*0.1)
mode = ["max ent"]
degrees.append(1)
mode = ["naive bayes"]
degrees.append(5)
None
mode = ["decision tree"]
SVMNumber = int(3000*3*0.6*0.6)
SVMNumber = int(3000*6*0.5*0.5)
SVMNumber = int(3000*4*0.9*0.9)
SVMMode = 'number'
degrees.append(1)
mode = ["decision tree"]
None

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

