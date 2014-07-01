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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc29Score.txt"
index = 29
gen = 0
prefix = ''
SVMNumber = int(3000*3*0.1*0.1)
degrees.append(7)
SVMMode = 'all'
SVMNumber = int(3000*5*0.2*0.2)
SVMNumber = int(3000*5*0.8*0.8)
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.4*0.4)
SVMMode = 'ratio'
None
mode = ["naive bayes"]
degrees.append(3)
degrees.append(5)
SVMNumber = int(3000*1*0.2*0.2)
degrees.append(4)
SVMNumber = int(3000*2*0.1*0.1)
SVMMode = 'all'
None
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

