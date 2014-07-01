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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun8Score.txt"
index = 8
gen = 0
prefix = ''
SVMNumber = int(3000*5*0.2*0.2)
None
SVMNumber = int(3000*3*0.4*0.4)
degrees.append(1)
None
SVMNumber = int(3000*6*0.9*0.9)
SVMNumber = int(2*2*0.2)
SVMNumber = int(2*2*0.7)
mode = ["max ent"]
SVMMode = 'number'
None
SVMNumber = int(3*3*0.7)
SVMMode = 'number'
SVMNumber = int(5*5*0.6)
SVMMode = 'number'
None
degrees.append(3)
mode = ["naive bayes"]
mode = ["max ent"]
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

