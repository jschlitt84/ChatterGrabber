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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun39Score.txt"
index = 39
gen = 0
prefix = ''
mode = ["svm"]
SVMNumber = int(3000*4*0.1*0.1)
degrees.append(3)
None
SVMMode = 'ratio'
SVMNumber = int(4*4*0.9)
None
mode = ["svm"]
SVMNumber = int(3000*3*0.5*0.5)
None
degrees.append(5)
None
degrees.append(1)
degrees.append(7)
None
mode = ["naive bayes"]
mode = ["svm"]
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.5*0.5)

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

