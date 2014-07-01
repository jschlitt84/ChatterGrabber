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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun26Score.txt"
index = 26
gen = 0
prefix = ''
degrees.append(7)
mode = ["naive bayes"]
SVMMode = 'number'
degrees.append(4)
degrees.append(4)
degrees.append(1)
mode = ["svm"]
mode = ["naive bayes"]
degrees.append(2)
degrees.append(5)
mode = ["naive bayes"]
degrees.append(4)
SVMNumber = int(3000*2*0.6*0.6)
degrees.append(7)
SVMNumber = int(3000*5*0.9*0.9)
SVMNumber = int(3*3*0.4)
None
degrees.append(4)
None
SVMNumber = int(3*3*0.1)

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

