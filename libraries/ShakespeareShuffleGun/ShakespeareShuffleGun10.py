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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun10Score.txt"
index = 10
gen = 0
prefix = ''
degrees.append(2)
SVMNumber = int(3000*6*0.2*0.2)
SVMNumber = int(3000*2*0.99*0.99)
degrees.append(6)
None
SVMNumber = int(7*7*0.8)
SVMMode = 'number'
SVMNumber = int(3000*4*0.2*0.2)
SVMMode = 'ratio'
SVMNumber = int(1*1*0.4)
SVMNumber = int(3000*7*0.6*0.6)
SVMNumber = int(7*7*0.7)
degrees.append(7)
SVMNumber = int(3000*5*0.4*0.4)
SVMNumber = int(7*7*0.7)
SVMNumber = int(3000*1*0.7*0.7)
SVMNumber = int(6*6*0.1)
degrees.append(4)
mode = ["naive bayes"]
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

