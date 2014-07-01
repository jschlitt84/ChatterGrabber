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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun15Score.txt"
index = 15
gen = 0
prefix = ''
SVMNumber = int(3000*3*0.2*0.2)
SVMNumber = int(3000*5*0.6*0.6)
degrees.append(4)
None
SVMMode = 'all'
degrees.append(2)
degrees.append(7)
degrees.append(1)
degrees.append(5)
mode = ["svm"]
mode = ["max ent"]
mode = ["svm"]
degrees.append(6)
SVMNumber = int(3000*7*0.4*0.4)
SVMNumber = int(3000*2*0.2*0.2)
SVMNumber = int(2*2*0.7)
None
SVMNumber = int(3000*3*0.1*0.1)
degrees.append(1)
SVMNumber = int(4*4*0.2)

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

