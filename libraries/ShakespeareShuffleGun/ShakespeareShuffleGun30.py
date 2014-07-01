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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun30Score.txt"
index = 30
gen = 0
prefix = ''
SVMNumber = int(3000*3*0.1*0.1)
None
degrees.append(4)
SVMNumber = int(3000*7*0.6*0.6)
None
SVMNumber = int(5*5*0.8)
SVMNumber = int(6*6*0.3)
SVMMode = 'all'
mode = ["naive bayes"]
SVMNumber = int(3000*1*0.7*0.7)
SVMNumber = int(3000*7*0.5*0.5)
SVMNumber = int(3000*6*0.3*0.3)
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(5)
SVMNumber = int(5*5*0.9)
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.4*0.4)
SVMNumber = int(4*4*0.99)
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

