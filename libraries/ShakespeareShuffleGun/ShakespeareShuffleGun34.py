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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun34Score.txt"
index = 34
gen = 0
prefix = ''
degrees.append(2)
None
SVMNumber = int(2*2*0.99)
SVMNumber = int(3000*6*0.6*0.6)
SVMMode = 'all'
mode = ["max ent"]
SVMMode = 'all'
SVMNumber = int(2*2*0.99)
SVMMode = 'number'
mode = ["naive bayes"]
SVMMode = 'all'
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.99*0.99)
SVMNumber = int(3000*5*0.3*0.3)
SVMMode = 'number'
degrees.append(6)
SVMNumber = int(3000*6*0.99*0.99)
SVMNumber = int(7*7*0.9)
degrees.append(2)
SVMNumber = int(3000*5*0.4*0.4)

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

