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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg34Score.txt"
index = 34
gen = 0
prefix = ''
mode = ["naive bayes"]
mode = ["svm"]
SVMNumber = int(3000*1*0.2*0.2)
SVMMode = 'all'
SVMNumber = int(4*4*0.8)
SVMNumber = int(6*6*0.3)
mode = ["naive bayes"]
SVMNumber = int(2*2*0.9)
None
degrees.append(4)
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'all'
SVMNumber = int(2*2*0.3)
degrees.append(5)
None
SVMMode = 'all'
degrees.append(1)
SVMMode = 'all'
SVMNumber = int(4*4*0.8)

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

