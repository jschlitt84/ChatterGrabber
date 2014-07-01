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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc5Score.txt"
index = 5
gen = 0
prefix = ''
SVMMode = 'number'
None
mode = ["max ent"]
SVMNumber = int(3000*2*0.6*0.6)
SVMMode = 'all'
degrees.append(4)
degrees.append(6)
SVMMode = 'number'
mode = ["svm"]
None
None
SVMNumber = int(3000*3*0.8*0.8)
SVMNumber = int(3000*4*0.5*0.5)
SVMNumber = int(3000*2*0.6*0.6)
None
mode = ["max ent"]
degrees.append(4)
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*4*0.5*0.5)

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

