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
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc24Score.txt"
index = 24
gen = 0
prefix = ''
None
SVMNumber = int(3000*7*0.5*0.5)
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.99*0.99)
degrees.append(4)
None
SVMNumber = int(3000*2*0.8*0.8)
degrees.append(6)
None
mode = ["svm"]
SVMMode = 'all'
mode = ["max ent"]
None
None
SVMMode = 'all'
mode = ["svm"]
mode = ["decision tree"]
SVMNumber = int(3000*1*0.4*0.4)
SVMNumber = int(3000*4*0.7*0.7)
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

