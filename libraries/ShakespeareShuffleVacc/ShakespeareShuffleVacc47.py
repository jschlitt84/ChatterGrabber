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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc47Score.txt"
index = 47
gen = 0
prefix = ''
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(6)
mode = ["decision tree"]
SVMNumber = int(3000*4*0.2*0.2)
None
SVMNumber = int(3000*5*0.99*0.99)
SVMMode = 'ratio'
degrees.append(4)
None
mode = ["max ent"]
SVMNumber = int(3000*3*0.3*0.3)
degrees.append(1)
None
degrees.append(3)
degrees.append(7)
degrees.append(6)
None
degrees.append(5)
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

