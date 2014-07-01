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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun11Score.txt"
index = 11
gen = 0
prefix = ''
SVMNumber = int(3000*1*0.6*0.6)
degrees.append(3)
None
SVMNumber = int(3000*3*0.9*0.9)
mode = ["svm"]
SVMMode = 'all'
mode = ["svm"]
SVMNumber = int(3000*2*0.5*0.5)
SVMMode = 'all'
None
None
SVMNumber = int(3000*7*0.4*0.4)
None
degrees.append(6)
SVMNumber = int(3000*3*0.4*0.4)
None
mode = ["max ent"]
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(4*4*0.2)

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

