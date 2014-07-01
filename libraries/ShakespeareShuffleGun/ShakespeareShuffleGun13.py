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
fileName = "ShakespeareShuffleGun/ShakespeareShuffleGun13Score.txt"
index = 13
gen = 0
prefix = ''
degrees.append(5)
mode = ["max ent"]
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(1)
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'number'
SVMNumber = int(1*1*0.7)
mode = ["naive bayes"]
degrees.append(1)
None
SVMMode = 'ratio'
mode = ["svm"]
None
SVMNumber = int(3000*3*0.5*0.5)
degrees.append(6)
None
SVMNumber = int(3000*6*0.4*0.4)
mode = ["naive bayes"]

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

