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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun40Score.txt"
index = 40
gen = 0
prefix = ''
SVMNumber = int(3000*5*0.3*0.3)
SVMMode = 'all'
None
SVMNumber = int(7*7*0.4)
SVMNumber = int(3000*7*0.99*0.99)
degrees.append(5)
degrees.append(3)
mode = ["svm"]
SVMNumber = int(4*4*0.4)
SVMNumber = int(3000*5*0.1*0.1)
SVMNumber = int(3000*6*0.1*0.1)
None
None
SVMNumber = int(1*1*0.1)
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(7*7*0.6)
SVMNumber = int(5*5*0.3)
SVMMode = 'ratio'
SVMNumber = int(1*1*0.5)

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

