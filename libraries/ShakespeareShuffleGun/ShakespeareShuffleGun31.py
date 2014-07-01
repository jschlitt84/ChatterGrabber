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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun31Score.txt"
index = 31
gen = 0
prefix = ''
degrees.append(4)
mode = ["max ent"]
degrees.append(4)
degrees.append(5)
mode = ["max ent"]
SVMMode = 'ratio'
None
mode = ["svm"]
SVMNumber = int(6*6*0.1)
SVMNumber = int(3*3*0.7)
SVMNumber = int(6*6*0.6)
None
SVMNumber = int(3*3*0.99)
degrees.append(7)
SVMNumber = int(7*7*0.4)
degrees.append(7)
SVMNumber = int(4*4*0.4)
None
SVMNumber = int(3000*1*0.7*0.7)
SVMNumber = int(6*6*0.1)

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

