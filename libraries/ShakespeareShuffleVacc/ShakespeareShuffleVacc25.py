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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc25Score.txt"
index = 25
gen = 0
prefix = ''
None
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.8*0.8)
mode = ["naive bayes"]
mode = ["max ent"]
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.3*0.3)
degrees.append(4)
SVMNumber = int(3000*2*0.9*0.9)
SVMMode = 'number'
None
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.8*0.8)
mode = ["decision tree"]
degrees.append(3)
mode = ["naive bayes"]
degrees.append(3)
None
SVMNumber = int(3000*2*0.4*0.4)
SVMNumber = int(3000*1*0.99*0.99)

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

