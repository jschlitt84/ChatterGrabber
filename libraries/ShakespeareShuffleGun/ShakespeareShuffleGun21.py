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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun21Score.txt"
index = 21
gen = 0
prefix = ''
mode = ["svm"]
None
SVMNumber = int(3000*2*0.5*0.5)
SVMNumber = int(2*2*0.1)
None
SVMNumber = int(6*6*0.8)
SVMNumber = int(3*3*0.5)
degrees.append(3)
mode = ["max ent"]
degrees.append(6)
SVMNumber = int(3000*3*0.8*0.8)
None
SVMNumber = int(5*5*0.5)
degrees.append(1)
SVMNumber = int(1*1*0.2)
degrees.append(1)
degrees.append(5)
None
None
SVMNumber = int(3000*2*0.5*0.5)

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

