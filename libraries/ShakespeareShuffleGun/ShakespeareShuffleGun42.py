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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun42Score.txt"
index = 42
gen = 0
prefix = ''
SVMNumber = int(6*6*0.99)
SVMMode = 'all'
None
SVMNumber = int(3000*1*0.4*0.4)
SVMNumber = int(7*7*0.6)
SVMNumber = int(3000*7*0.8*0.8)
degrees.append(4)
SVMNumber = int(3*3*0.2)
SVMNumber = int(7*7*0.8)
SVMNumber = int(3000*1*0.7*0.7)
None
SVMMode = 'ratio'
SVMNumber = int(2*2*0.99)
SVMNumber = int(6*6*0.5)
mode = ["naive bayes"]
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMMode = 'number'
degrees.append(2)
SVMNumber = int(3000*3*0.5*0.5)

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

