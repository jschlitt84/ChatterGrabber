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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun2Score.txt"
index = 2
gen = 0
prefix = ''
SVMNumber = int(3000*2*0.8*0.8)
SVMNumber = int(7*7*0.1)
SVMNumber = int(4*4*0.8)
None
degrees.append(3)
SVMMode = 'number'
SVMNumber = int(3000*3*0.3*0.3)
SVMNumber = int(2*2*0.2)
SVMMode = 'ratio'
mode = ["max ent"]
mode = ["max ent"]
degrees.append(4)
SVMNumber = int(3000*4*0.9*0.9)
degrees.append(5)
SVMMode = 'number'
degrees.append(4)
degrees.append(7)
SVMMode = 'ratio'
None
SVMNumber = int(3000*4*0.99*0.99)

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

