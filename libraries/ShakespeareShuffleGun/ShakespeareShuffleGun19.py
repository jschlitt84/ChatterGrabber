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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun19Score.txt"
index = 19
gen = 0
prefix = ''
SVMNumber = int(3000*3*0.3*0.3)
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.9*0.9)
mode = ["max ent"]
None
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(7)
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(4*4*0.3)
degrees.append(6)
SVMNumber = int(2*2*0.2)
SVMNumber = int(4*4*0.6)
degrees.append(4)
mode = ["svm"]
SVMNumber = int(2*2*0.2)
SVMNumber = int(3000*6*0.9*0.9)
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.4*0.4)
SVMNumber = int(1*1*0.8)

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

