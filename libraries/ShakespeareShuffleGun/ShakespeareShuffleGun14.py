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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun14Score.txt"
index = 14
gen = 0
prefix = ''
mode = ["max ent"]
SVMMode = 'all'
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(7)
None
mode = ["max ent"]
None
SVMNumber = int(7*7*0.2)
SVMNumber = int(5*5*0.7)
SVMNumber = int(3000*6*0.4*0.4)
None
SVMNumber = int(3000*7*0.6*0.6)
SVMNumber = int(3000*7*0.1*0.1)
None
SVMMode = 'ratio'
None
degrees.append(3)
mode = ["svm"]
SVMNumber = int(7*7*0.8)

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

