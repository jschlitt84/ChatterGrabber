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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc3Score.txt"
index = 3
gen = 0
prefix = ''
None
mode = ["max ent"]
SVMNumber = int(3000*4*0.99*0.99)
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(3)
None
degrees.append(3)
degrees.append(6)
degrees.append(2)
degrees.append(5)
None
mode = ["svm"]
SVMMode = 'number'
SVMNumber = int(3000*1*0.5*0.5)
degrees.append(7)
SVMNumber = int(3000*2*0.8*0.8)
SVMNumber = int(3000*6*0.6*0.6)
mode = ["decision tree"]
None
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

