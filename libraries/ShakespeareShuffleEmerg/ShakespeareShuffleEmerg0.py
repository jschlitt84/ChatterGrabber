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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg0Score.txt"
index = 0
gen = 0
prefix = ''
mode = ["max ent"]
degrees.append(5)
degrees.append(5)
None
None
mode = ["max ent"]
degrees.append(4)
None
SVMNumber = int(5*5*0.5)
None
SVMNumber = int(5*5*0.1)
SVMMode = 'number'
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.9*0.9)
SVMNumber = int(3000*4*0.6*0.6)
None
degrees.append(3)
None
mode = ["svm"]
SVMMode = 'number'

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

