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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun28Score.txt"
index = 28
gen = 0
prefix = ''
None
SVMNumber = int(3000*6*0.1*0.1)
mode = ["max ent"]
None
SVMNumber = int(4*4*0.9)
None
SVMNumber = int(3000*5*0.1*0.1)
None
degrees.append(3)
SVMNumber = int(5*5*0.7)
SVMNumber = int(3000*4*0.9*0.9)
SVMMode = 'number'
None
degrees.append(1)
SVMNumber = int(4*4*0.99)
SVMNumber = int(3000*1*0.9*0.9)
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*7*0.99*0.99)
None
SVMMode = 'ratio'

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

