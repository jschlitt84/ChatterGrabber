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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun43Score.txt"
index = 43
gen = 0
prefix = ''
degrees.append(1)
SVMNumber = int(7*7*0.1)
SVMNumber = int(3000*3*0.6*0.6)
SVMNumber = int(2*2*0.9)
SVMNumber = int(4*4*0.1)
SVMNumber = int(3000*2*0.99*0.99)
SVMNumber = int(3000*6*0.9*0.9)
SVMMode = 'ratio'
SVMNumber = int(5*5*0.3)
SVMNumber = int(4*4*0.7)
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(3000*4*0.3*0.3)
SVMNumber = int(3000*4*0.4*0.4)
SVMMode = 'all'
SVMNumber = int(3*3*0.8)
None
None
SVMNumber = int(2*2*0.99)
None

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

