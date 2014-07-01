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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun22Score.txt"
index = 22
gen = 0
prefix = ''
SVMMode = 'ratio'
None
mode = ["max ent"]
SVMNumber = int(3*3*0.99)
degrees.append(2)
SVMNumber = int(3000*5*0.2*0.2)
degrees.append(1)
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(3000*5*0.5*0.5)
None
SVMMode = 'number'
SVMNumber = int(3000*4*0.3*0.3)
None
mode = ["max ent"]
None
degrees.append(2)
SVMMode = 'all'
SVMMode = 'all'
None
mode = ["svm"]

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

