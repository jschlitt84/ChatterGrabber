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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg19Score.txt"
index = 19
gen = 0
prefix = ''
SVMMode = 'ratio'
degrees.append(1)
None
SVMMode = 'number'
SVMNumber = int(3000*6*0.8*0.8)
mode = ["svm"]
None
SVMNumber = int(3000*7*0.6*0.6)
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMNumber = int(3000*2*0.9*0.9)
SVMNumber = int(3000*7*0.99*0.99)
None
mode = ["svm"]
None
mode = ["svm"]
degrees.append(2)
degrees.append(1)
mode = ["naive bayes"]
degrees.append(4)

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

