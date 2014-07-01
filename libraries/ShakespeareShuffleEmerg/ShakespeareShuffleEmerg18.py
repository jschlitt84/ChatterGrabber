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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg18Score.txt"
index = 18
gen = 0
prefix = ''
mode = ["naive bayes"]
degrees.append(5)
degrees.append(3)
SVMMode = 'number'
mode = ["max ent"]
SVMMode = 'all'
mode = ["max ent"]
None
mode = ["naive bayes"]
None
SVMMode = 'number'
degrees.append(5)
mode = ["svm"]
SVMMode = 'ratio'
mode = ["max ent"]
SVMMode = 'all'
None
SVMNumber = int(6*6*0.8)
SVMMode = 'ratio'
SVMNumber = int(1*1*0.4)

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

