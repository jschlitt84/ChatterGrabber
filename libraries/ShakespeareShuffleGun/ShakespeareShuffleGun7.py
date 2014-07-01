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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun7Score.txt"
index = 7
gen = 0
prefix = ''
SVMMode = 'number'
SVMMode = 'number'
degrees.append(2)
SVMMode = 'number'
degrees.append(1)
mode = ["max ent"]
mode = ["max ent"]
degrees.append(5)
degrees.append(5)
mode = ["naive bayes"]
SVMMode = 'ratio'
None
SVMNumber = int(6*6*0.9)
SVMNumber = int(3000*6*0.8*0.8)
SVMNumber = int(2*2*0.5)
mode = ["svm"]
None
SVMNumber = int(3000*5*0.4*0.4)
SVMNumber = int(3000*3*0.99*0.99)
SVMNumber = int(3000*1*0.5*0.5)

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

