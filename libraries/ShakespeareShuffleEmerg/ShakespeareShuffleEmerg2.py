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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg2Score.txt"
index = 2
gen = 0
prefix = ''
SVMNumber = int(5*5*0.6)
degrees.append(5)
SVMNumber = int(2*2*0.1)
SVMMode = 'all'
SVMNumber = int(6*6*0.1)
SVMNumber = int(5*5*0.7)
SVMNumber = int(1*1*0.3)
degrees.append(2)
degrees.append(5)
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.9*0.9)
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMNumber = int(3000*2*0.99*0.99)
None
SVMMode = 'number'
SVMNumber = int(6*6*0.3)
SVMNumber = int(1*1*0.1)
SVMNumber = int(6*6*0.99)
mode = ["naive bayes"]

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

