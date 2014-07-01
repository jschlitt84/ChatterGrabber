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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun1Score.txt"
index = 1
gen = 0
prefix = ''
mode = ["svm"]
SVMNumber = int(6*6*0.3)
mode = ["svm"]
mode = ["svm"]
None
degrees.append(1)
SVMNumber = int(3000*5*0.3*0.3)
SVMNumber = int(1*1*0.9)
mode = ["svm"]
SVMMode = 'all'
None
mode = ["naive bayes"]
SVMMode = 'number'
SVMNumber = int(3000*3*0.9*0.9)
mode = ["max ent"]
mode = ["naive bayes"]
None
None
SVMNumber = int(2*2*0.7)
mode = ["naive bayes"]

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

