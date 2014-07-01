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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc30Score.txt"
index = 30
gen = 0
prefix = ''
SVMNumber = int(3000*1*0.3*0.3)
SVMNumber = int(3000*5*0.5*0.5)
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.8*0.8)
SVMMode = 'number'
degrees.append(5)
None
mode = ["max ent"]
degrees.append(5)
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.99*0.99)
SVMMode = 'number'
SVMNumber = int(3000*5*0.3*0.3)
SVMMode = 'all'
degrees.append(1)
None
None
SVMNumber = int(3000*2*0.8*0.8)
None
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

