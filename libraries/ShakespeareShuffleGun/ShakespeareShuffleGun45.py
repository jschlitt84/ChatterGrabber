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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun45Score.txt"
index = 45
gen = 0
prefix = ''
mode = ["svm"]
SVMNumber = int(3000*7*0.9*0.9)
SVMMode = 'number'
mode = ["svm"]
SVMNumber = int(7*7*0.6)
SVMNumber = int(3*3*0.1)
SVMNumber = int(3000*1*0.5*0.5)
degrees.append(5)
SVMMode = 'ratio'
None
None
SVMNumber = int(4*4*0.4)
degrees.append(4)
SVMNumber = int(1*1*0.6)
SVMMode = 'all'
None
mode = ["naive bayes"]
mode = ["max ent"]
mode = ["svm"]
SVMNumber = int(3000*2*0.4*0.4)

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

