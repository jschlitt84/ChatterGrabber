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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg15Score.txt"
index = 15
gen = 3
prefix = ''
SVMNumber = int(4*4*0.7)
degrees.append(7)
SVMMode = 'number'
SVMNumber = int(3000*3*0.4*0.4)
degrees.append(4)
SVMNumber = int(6*6*0.3)
mode = ["naive bayes"]
SVMMode = 'all'
degrees.append(4)
degrees.append(4)
SVMMode = 'ratio'
None
SVMMode = 'number'
SVMNumber = int(3000*5*0.7*0.7)
mode = ["svm"]
None
SVMNumber = int(4*4*0.4)
SVMNumber = int(5*5*0.99)
SVMMode = 'all'
SVMMode = 'ratio'

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

