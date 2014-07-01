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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc2Score.txt"
index = 2
gen = 0
prefix = ''
degrees.append(6)
mode = ["max ent"]
mode = ["max ent"]
SVMNumber = int(3000*6*0.1*0.1)
SVMMode = 'number'
mode = ["max ent"]
mode = ["max ent"]
SVMMode = 'number'
degrees.append(5)
SVMNumber = int(3000*4*0.1*0.1)
mode = ["svm"]
SVMMode = 'number'
degrees.append(3)
None
SVMNumber = int(3000*4*0.1*0.1)
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*1*0.6*0.6)
SVMNumber = int(3000*7*0.99*0.99)
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

