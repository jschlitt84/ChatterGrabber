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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun4Score.txt"
index = 4
gen = 0
prefix = ''
SVMMode = 'ratio'
None
SVMNumber = int(2*2*0.8)
SVMNumber = int(3000*2*0.9*0.9)
None
SVMNumber = int(3000*1*0.9*0.9)
None
None
SVMMode = 'number'
SVMNumber = int(7*7*0.1)
SVMNumber = int(3000*1*0.3*0.3)
SVMMode = 'number'
None
degrees.append(5)
SVMNumber = int(3*3*0.6)
SVMMode = 'ratio'
SVMNumber = int(3000*5*0.99*0.99)
SVMNumber = int(4*4*0.4)
mode = ["max ent"]
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

