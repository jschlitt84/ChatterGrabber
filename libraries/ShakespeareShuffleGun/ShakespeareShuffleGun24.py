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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun24Score.txt"
index = 24
gen = 0
prefix = ''
None
SVMMode = 'all'
SVMNumber = int(6*6*0.9)
SVMMode = 'number'
mode = ["naive bayes"]
None
SVMNumber = int(3*3*0.7)
SVMMode = 'ratio'
None
None
degrees.append(7)
degrees.append(6)
degrees.append(1)
SVMNumber = int(3000*2*0.7*0.7)
SVMNumber = int(3000*7*0.8*0.8)
SVMNumber = int(5*5*0.6)
SVMNumber = int(5*5*0.9)
SVMNumber = int(3*3*0.9)
SVMNumber = int(2*2*0.8)
SVMNumber = int(3000*3*0.8*0.8)

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

