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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc32Score.txt"
index = 32
gen = 0
prefix = ''
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*7*0.5*0.5)
degrees.append(4)
SVMNumber = int(3000*3*0.2*0.2)
SVMNumber = int(3000*7*0.6*0.6)
degrees.append(5)
None
SVMMode = 'all'
SVMNumber = int(3000*6*0.1*0.1)
SVMNumber = int(3000*6*0.99*0.99)
None
degrees.append(4)
SVMNumber = int(3000*5*0.1*0.1)
SVMNumber = int(3000*1*0.6*0.6)
SVMMode = 'all'
mode = ["max ent"]
SVMNumber = int(3000*3*0.9*0.9)
mode = ["svm"]
SVMMode = 'all'
degrees.append(3)

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

