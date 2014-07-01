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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun35Score.txt"
index = 35
gen = 0
prefix = ''
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(1*1*0.7)
mode = ["naive bayes"]
degrees.append(4)
None
degrees.append(1)
None
degrees.append(2)
SVMNumber = int(3*3*0.3)
SVMNumber = int(1*1*0.6)
mode = ["svm"]
SVMNumber = int(3000*4*0.3*0.3)
None
None
SVMNumber = int(3000*3*0.3*0.3)
degrees.append(2)
SVMNumber = int(3*3*0.6)
mode = ["naive bayes"]
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

