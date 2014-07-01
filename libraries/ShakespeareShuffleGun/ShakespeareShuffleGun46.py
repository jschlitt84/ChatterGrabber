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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun46Score.txt"
index = 46
gen = 0
prefix = ''
SVMNumber = int(3000*6*0.3*0.3)
SVMMode = 'number'
SVMNumber = int(3000*5*0.2*0.2)
degrees.append(7)
None
mode = ["svm"]
degrees.append(7)
None
SVMMode = 'number'
SVMMode = 'ratio'
mode = ["svm"]
SVMNumber = int(3000*6*0.3*0.3)
None
degrees.append(7)
None
None
SVMMode = 'all'
degrees.append(3)
SVMNumber = int(6*6*0.8)
degrees.append(7)

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

