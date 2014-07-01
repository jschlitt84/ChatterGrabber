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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun49Score.txt"
index = 49
gen = 0
prefix = ''
None
SVMMode = 'all'
degrees.append(6)
SVMMode = 'number'
mode = ["naive bayes"]
SVMMode = 'all'
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(4)
mode = ["svm"]
None
mode = ["svm"]
SVMMode = 'ratio'
SVMNumber = int(3000*7*0.8*0.8)
SVMMode = 'all'
SVMNumber = int(3000*6*0.2*0.2)
degrees.append(5)
degrees.append(6)
SVMMode = 'ratio'
SVMNumber = int(3000*2*0.3*0.3)

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

