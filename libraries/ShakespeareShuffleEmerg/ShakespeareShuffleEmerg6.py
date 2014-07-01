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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg6Score.txt"
index = 6
gen = 4
prefix = ''
SVMNumber = int(4*4*0.5)
SVMMode = 'ratio'
None
mode = ["svm"]
SVMNumber = int(5*5*0.4)
SVMMode = 'all'
None
mode = ["max ent"]
degrees.append(6)
None
SVMMode = 'all'
None
None
SVMNumber = int(3000*3*0.7*0.7)
SVMNumber = int(3000*5*0.6*0.6)
mode = ["naive bayes"]
SVMMode = 'number'
None
degrees.append(1)
mode = ["svm"]

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

