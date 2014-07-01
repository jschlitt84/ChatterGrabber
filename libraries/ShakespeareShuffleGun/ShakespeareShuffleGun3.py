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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun3Score.txt"
index = 3
gen = 0
prefix = ''
degrees.append(4)
SVMNumber = int(3000*2*0.7*0.7)
SVMMode = 'number'
mode = ["naive bayes"]
SVMMode = 'ratio'
mode = ["svm"]
None
SVMNumber = int(1*1*0.8)
degrees.append(3)
mode = ["svm"]
None
degrees.append(3)
mode = ["naive bayes"]
None
SVMMode = 'number'
SVMNumber = int(1*1*0.8)
None
SVMNumber = int(3000*7*0.6*0.6)
None
degrees.append(2)

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

