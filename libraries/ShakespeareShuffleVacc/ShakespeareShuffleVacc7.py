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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc7Score.txt"
index = 7
gen = 0
prefix = ''
None
SVMMode = 'all'
degrees.append(6)
SVMMode = 'all'
SVMMode = 'number'
mode = ["svm"]
SVMNumber = int(3000*6*0.8*0.8)
SVMMode = 'all'
degrees.append(4)
degrees.append(2)
SVMMode = 'ratio'
None
SVMNumber = int(3000*7*0.9*0.9)
SVMNumber = int(3000*2*0.9*0.9)
SVMNumber = int(3000*5*0.8*0.8)
None
mode = ["max ent"]
SVMNumber = int(3000*6*0.99*0.99)
SVMMode = 'number'
SVMMode = 'ratio'

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

