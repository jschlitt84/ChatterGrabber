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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun20Score.txt"
index = 20
gen = 0
prefix = ''
mode = ["svm"]
None
SVMMode = 'number'
SVMNumber = int(3000*7*0.99*0.99)
SVMNumber = int(3000*6*0.99*0.99)
SVMNumber = int(3000*3*0.9*0.9)
SVMNumber = int(5*5*0.4)
SVMMode = 'number'
mode = ["naive bayes"]
mode = ["max ent"]
SVMNumber = int(7*7*0.6)
degrees.append(2)
SVMNumber = int(5*5*0.4)
SVMMode = 'number'
None
degrees.append(7)
SVMMode = 'number'
mode = ["max ent"]
degrees.append(1)
SVMNumber = int(3000*6*0.3*0.3)

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

