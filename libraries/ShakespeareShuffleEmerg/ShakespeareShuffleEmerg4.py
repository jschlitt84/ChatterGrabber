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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg4Score.txt"
index = 4
gen = 0
prefix = ''
SVMMode = 'number'
mode = ["svm"]
None
SVMNumber = int(4*4*0.99)
None
mode = ["svm"]
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.9*0.9)
SVMNumber = int(3*3*0.2)
None
SVMMode = 'all'
SVMNumber = int(3*3*0.3)
None
SVMNumber = int(6*6*0.99)
mode = ["max ent"]
SVMNumber = int(3000*7*0.99*0.99)
degrees.append(4)
SVMMode = 'ratio'
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

