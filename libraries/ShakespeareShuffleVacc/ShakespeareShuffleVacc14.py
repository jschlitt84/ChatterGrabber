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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc14Score.txt"
index = 14
gen = 0
prefix = ''
None
None
mode = ["svm"]
SVMMode = 'all'
SVMNumber = int(3000*1*0.9*0.9)
degrees.append(5)
SVMMode = 'number'
SVMNumber = int(3000*2*0.7*0.7)
mode = ["max ent"]
mode = ["max ent"]
degrees.append(5)
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*4*0.6*0.6)
degrees.append(1)
degrees.append(7)
SVMNumber = int(3000*1*0.6*0.6)
degrees.append(7)
mode = ["max ent"]
degrees.append(5)
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

