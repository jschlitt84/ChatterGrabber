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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun27Score.txt"
index = 27
gen = 0
prefix = ''
degrees.append(3)
SVMNumber = int(3000*7*0.6*0.6)
SVMNumber = int(6*6*0.3)
degrees.append(5)
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(6)
SVMNumber = int(3000*2*0.3*0.3)
degrees.append(1)
None
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'number'
None
None
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.1*0.1)
SVMNumber = int(4*4*0.2)
SVMNumber = int(6*6*0.8)
SVMNumber = int(6*6*0.2)
SVMMode = 'ratio'

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

