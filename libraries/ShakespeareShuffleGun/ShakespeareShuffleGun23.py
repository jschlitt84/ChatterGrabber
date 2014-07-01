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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun23Score.txt"
index = 23
gen = 0
prefix = ''
SVMMode = 'all'
SVMNumber = int(3*3*0.7)
degrees.append(3)
SVMNumber = int(2*2*0.1)
None
SVMNumber = int(3000*2*0.7*0.7)
None
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'number'
SVMNumber = int(3000*5*0.3*0.3)
degrees.append(7)
SVMNumber = int(3000*2*0.7*0.7)
SVMNumber = int(3000*7*0.5*0.5)
None
degrees.append(4)
degrees.append(5)
degrees.append(7)
SVMMode = 'ratio'
SVMNumber = int(6*6*0.4)

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

