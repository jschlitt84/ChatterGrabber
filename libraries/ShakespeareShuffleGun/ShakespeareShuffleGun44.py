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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun44Score.txt"
index = 44
gen = 0
prefix = ''
SVMNumber = int(3000*5*0.7*0.7)
SVMMode = 'all'
mode = ["naive bayes"]
SVMNumber = int(6*6*0.9)
SVMMode = 'ratio'
SVMNumber = int(6*6*0.8)
None
degrees.append(4)
mode = ["max ent"]
mode = ["svm"]
degrees.append(7)
degrees.append(5)
degrees.append(4)
None
mode = ["svm"]
None
degrees.append(2)
SVMNumber = int(3000*4*0.9*0.9)
SVMNumber = int(1*1*0.5)
degrees.append(3)

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

