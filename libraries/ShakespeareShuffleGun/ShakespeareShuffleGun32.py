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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun32Score.txt"
index = 32
gen = 0
prefix = ''
SVMNumber = int(3*3*0.2)
None
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.3*0.3)
degrees.append(4)
SVMNumber = int(3000*4*0.5*0.5)
None
mode = ["naive bayes"]
SVMMode = 'number'
None
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(2*2*0.1)
degrees.append(6)
mode = ["svm"]
SVMNumber = int(2*2*0.4)
degrees.append(6)
None
mode = ["naive bayes"]
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

