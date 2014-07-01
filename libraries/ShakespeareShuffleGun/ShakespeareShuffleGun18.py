from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['GunTrackerNLTK.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun18Score.txt"
index = 18
gen = 0
prefix = ''
degrees.append(7)
mode = ["max ent"]
None
None
SVMNumber = int(6*6*0.6)
mode = ["max ent"]
SVMNumber = int(3*3*0.8)
degrees.append(4)
None
SVMNumber = int(3000*3*0.4*0.4)
None
mode = ["naive bayes"]
mode = ["naive bayes"]
mode = ["svm"]
SVMNumber = int(3000*5*0.9*0.9)
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["naive bayes"]
mode = ["max ent"]
SVMNumber = int(3000*5*0.8*0.8)

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

