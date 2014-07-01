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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg14Score.txt"
index = 14
gen = 5
prefix = ''
mode = ["svm"]
degrees.append(4)
None
SVMNumber = int(4*4*0.99)
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(4)
None
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(4*4*0.4)
degrees.append(1)
SVMMode = 'ratio'
None
None
SVMNumber = int(3000*7*0.7*0.7)
mode = ["svm"]
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.8*0.8)
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

