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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg16Score.txt"
index = 16
gen = 0
prefix = ''
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.1*0.1)
degrees.append(2)
SVMNumber = int(3*3*0.9)
mode = ["svm"]
SVMNumber = int(6*6*0.4)
SVMNumber = int(3000*5*0.99*0.99)
degrees.append(2)
None
SVMMode = 'all'
SVMNumber = int(3000*1*0.1*0.1)
SVMNumber = int(3000*6*0.99*0.99)
None
degrees.append(1)
None
degrees.append(7)
mode = ["naive bayes"]
SVMNumber = int(7*7*0.8)
mode = ["svm"]
SVMNumber = int(6*6*0.5)

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

