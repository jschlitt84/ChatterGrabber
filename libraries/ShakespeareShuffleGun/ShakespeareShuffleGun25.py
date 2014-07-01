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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun25Score.txt"
index = 25
gen = 0
prefix = ''
SVMNumber = int(3000*2*0.9*0.9)
degrees.append(1)
None
None
SVMNumber = int(3*3*0.2)
None
SVMNumber = int(5*5*0.2)
SVMNumber = int(3000*2*0.4*0.4)
mode = ["svm"]
None
SVMNumber = int(3000*5*0.4*0.4)
SVMMode = 'all'
SVMNumber = int(3000*5*0.7*0.7)
mode = ["naive bayes"]
degrees.append(7)
SVMNumber = int(2*2*0.7)
degrees.append(1)
degrees.append(2)
SVMMode = 'ratio'
mode = ["max ent"]

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

