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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun6Score.txt"
index = 6
gen = 0
prefix = ''
SVMNumber = int(4*4*0.9)
SVMMode = 'all'
degrees.append(1)
SVMNumber = int(3000*6*0.9*0.9)
mode = ["svm"]
SVMNumber = int(3000*5*0.6*0.6)
SVMNumber = int(3000*6*0.3*0.3)
None
None
degrees.append(4)
None
SVMMode = 'number'
mode = ["svm"]
degrees.append(4)
mode = ["svm"]
SVMNumber = int(1*1*0.8)
SVMNumber = int(4*4*0.1)
SVMMode = 'ratio'
mode = ["naive bayes"]
mode = ["max ent"]

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

