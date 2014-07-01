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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun37Score.txt"
index = 37
gen = 0
prefix = ''
degrees.append(2)
mode = ["naive bayes"]
None
SVMNumber = int(6*6*0.3)
mode = ["svm"]
SVMNumber = int(3000*2*0.3*0.3)
mode = ["svm"]
degrees.append(7)
SVMMode = 'all'
SVMNumber = int(3*3*0.2)
SVMNumber = int(3000*3*0.8*0.8)
SVMNumber = int(3000*6*0.6*0.6)
None
mode = ["svm"]
mode = ["svm"]
SVMMode = 'number'
None
SVMMode = 'all'
SVMNumber = int(7*7*0.8)
SVMNumber = int(3000*4*0.7*0.7)

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

