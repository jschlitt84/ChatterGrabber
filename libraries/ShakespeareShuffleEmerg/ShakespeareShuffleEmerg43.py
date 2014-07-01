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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg43Score.txt"
index = 43
gen = 0
prefix = ''
SVMNumber = int(2*2*0.99)
degrees.append(4)
degrees.append(6)
None
None
degrees.append(2)
SVMNumber = int(3000*3*0.5*0.5)
None
mode = ["svm"]
SVMNumber = int(3*3*0.7)
None
degrees.append(6)
mode = ["svm"]
SVMNumber = int(3000*6*0.9*0.9)
SVMNumber = int(2*2*0.2)
mode = ["naive bayes"]
degrees.append(1)
SVMNumber = int(3000*7*0.2*0.2)
degrees.append(6)
SVMNumber = int(4*4*0.4)

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

