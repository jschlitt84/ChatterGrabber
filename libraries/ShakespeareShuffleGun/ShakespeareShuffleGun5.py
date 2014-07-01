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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun5Score.txt"
index = 5
gen = 0
prefix = ''
mode = ["svm"]
mode = ["svm"]
None
None
SVMNumber = int(3*3*0.5)
SVMNumber = int(3000*4*0.4*0.4)
SVMNumber = int(6*6*0.2)
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(6*6*0.5)
degrees.append(3)
SVMMode = 'all'
SVMNumber = int(3000*5*0.8*0.8)
SVMNumber = int(3*3*0.1)
None
None
degrees.append(6)
None
SVMNumber = int(2*2*0.4)
SVMNumber = int(3000*2*0.4*0.4)

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

