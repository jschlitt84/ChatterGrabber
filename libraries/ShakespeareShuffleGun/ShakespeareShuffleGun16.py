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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun16Score.txt"
index = 16
gen = 0
prefix = ''
degrees.append(6)
None
None
SVMNumber = int(3000*2*0.5*0.5)
SVMNumber = int(3*3*0.6)
None
None
None
degrees.append(3)
mode = ["naive bayes"]
None
SVMNumber = int(3000*4*0.5*0.5)
SVMNumber = int(5*5*0.5)
None
degrees.append(3)
None
degrees.append(7)
SVMNumber = int(3000*6*0.2*0.2)
SVMMode = 'number'
mode = ["max ent"]

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

