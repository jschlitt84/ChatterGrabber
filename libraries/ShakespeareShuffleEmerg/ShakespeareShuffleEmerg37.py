from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['EmergNLTKScoring.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg37Score.txt"
index = 37
gen = 3
prefix = ''
SVMMode = 'number'
degrees.append(5)
SVMNumber = int(3000*3*0.4*0.4)
degrees.append(3)
degrees.append(2)
SVMMode = 'all'
mode = ["max ent"]
None
SVMMode = 'all'
None
degrees.append(4)
degrees.append(5)
mode = ["naive bayes"]
degrees.append(7)
mode = ["svm"]
SVMNumber = int(2*2*0.2)
mode = ["naive bayes"]
SVMMode = 'ratio'
degrees.append(6)
None

outFile = open(fileName,'w')
cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber,
	'SVMOrder':'GVTMACFSNN'}
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

