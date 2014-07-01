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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc12Score.txt"
index = 12
gen = 0
prefix = ''
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(4)
degrees.append(4)
None
SVMNumber = int(3000*4*0.4*0.4)
SVMMode = 'all'
SVMNumber = int(3000*4*0.4*0.4)
degrees.append(4)
None
SVMNumber = int(3000*6*0.7*0.7)
SVMMode = 'all'
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(4)
None
None
mode = ["decision tree"]
mode = ["max ent"]
SVMMode = 'number'

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

