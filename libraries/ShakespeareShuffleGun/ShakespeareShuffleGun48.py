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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun48Score.txt"
index = 48
gen = 0
prefix = ''
SVMNumber = int(3000*7*0.4*0.4)
mode = ["svm"]
SVMMode = 'all'
degrees.append(5)
None
SVMMode = 'number'
SVMNumber = int(6*6*0.4)
degrees.append(2)
mode = ["max ent"]
SVMNumber = int(3000*6*0.5*0.5)
SVMMode = 'number'
degrees.append(2)
mode = ["svm"]
degrees.append(3)
SVMMode = 'all'
mode = ["max ent"]
SVMNumber = int(3000*6*0.4*0.4)
None
degrees.append(4)
SVMNumber = int(2*2*0.99)

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

