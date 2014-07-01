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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun0Score.txt"
index = 0
gen = 0
prefix = ''
mode = ["naive bayes"]
None
SVMMode = 'ratio'
mode = ["naive bayes"]
None
SVMNumber = int(3*3*0.6)
degrees.append(4)
None
degrees.append(6)
None
degrees.append(2)
SVMNumber = int(3000*2*0.7*0.7)
SVMNumber = int(3000*1*0.2*0.2)
degrees.append(2)
SVMMode = 'ratio'
SVMMode = 'ratio'
degrees.append(4)
SVMNumber = int(3000*4*0.4*0.4)
SVMNumber = int(3000*3*0.4*0.4)
None

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

