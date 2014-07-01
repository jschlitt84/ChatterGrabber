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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc20Score.txt"
index = 20
gen = 0
prefix = ''
degrees.append(5)
degrees.append(4)
SVMNumber = int(3000*4*0.2*0.2)
None
degrees.append(5)
SVMNumber = int(3000*7*0.3*0.3)
SVMNumber = int(3000*5*0.7*0.7)
SVMNumber = int(3000*3*0.8*0.8)
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*2*0.3*0.3)
degrees.append(3)
SVMNumber = int(3000*3*0.9*0.9)
mode = ["decision tree"]
mode = ["svm"]
degrees.append(7)
degrees.append(6)
SVMNumber = int(3000*3*0.1*0.1)
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

