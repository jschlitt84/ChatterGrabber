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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun17Score.txt"
index = 17
gen = 0
prefix = ''
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.99*0.99)
SVMMode = 'all'
SVMNumber = int(3000*1*0.2*0.2)
degrees.append(7)
SVMNumber = int(3000*6*0.1*0.1)
SVMMode = 'ratio'
degrees.append(1)
SVMNumber = int(3000*2*0.7*0.7)
None
SVMNumber = int(5*5*0.99)
SVMNumber = int(2*2*0.1)
SVMNumber = int(4*4*0.1)
None
mode = ["naive bayes"]
SVMNumber = int(3*3*0.7)
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.99*0.99)
SVMMode = 'number'
degrees.append(1)

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

