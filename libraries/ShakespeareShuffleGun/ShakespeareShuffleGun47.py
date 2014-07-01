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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun47Score.txt"
index = 47
gen = 0
prefix = ''
SVMMode = 'number'
SVMNumber = int(3000*7*0.2*0.2)
SVMMode = 'all'
None
SVMMode = 'ratio'
None
None
SVMNumber = int(3000*1*0.6*0.6)
degrees.append(3)
SVMNumber = int(3000*5*0.6*0.6)
SVMMode = 'number'
degrees.append(6)
SVMNumber = int(3000*6*0.3*0.3)
degrees.append(7)
degrees.append(6)
SVMNumber = int(3000*4*0.3*0.3)
mode = ["max ent"]
degrees.append(6)
SVMMode = 'number'
SVMNumber = int(3*3*0.5)

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

