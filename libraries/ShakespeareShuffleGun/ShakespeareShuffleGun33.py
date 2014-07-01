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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun33Score.txt"
index = 33
gen = 0
prefix = ''
None
None
mode = ["naive bayes"]
degrees.append(5)
None
degrees.append(6)
SVMMode = 'number'
SVMMode = 'ratio'
SVMMode = 'number'
SVMNumber = int(3000*1*0.6*0.6)
SVMMode = 'ratio'
degrees.append(4)
SVMMode = 'number'
mode = ["max ent"]
mode = ["naive bayes"]
SVMNumber = int(1*1*0.5)
SVMNumber = int(3000*1*0.4*0.4)
mode = ["naive bayes"]
None
SVMNumber = int(4*4*0.99)

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

