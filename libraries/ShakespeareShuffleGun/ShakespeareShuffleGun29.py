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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun29Score.txt"
index = 29
gen = 0
prefix = ''
SVMNumber = int(7*7*0.9)
degrees.append(7)
None
degrees.append(5)
mode = ["svm"]
degrees.append(6)
None
mode = ["naive bayes"]
None
SVMNumber = int(3000*1*0.6*0.6)
SVMNumber = int(2*2*0.6)
None
mode = ["naive bayes"]
mode = ["max ent"]
SVMMode = 'number'
degrees.append(2)
SVMMode = 'number'
SVMMode = 'all'
SVMMode = 'number'
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

