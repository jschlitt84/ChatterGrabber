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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg13Score.txt"
index = 13
gen = 0
prefix = ''
degrees.append(5)
mode = ["max ent"]
degrees.append(7)
degrees.append(6)
degrees.append(2)
degrees.append(1)
SVMNumber = int(3000*7*0.4*0.4)
None
degrees.append(7)
SVMNumber = int(2*2*0.3)
SVMNumber = int(1*1*0.1)
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMNumber = int(1*1*0.9)
SVMNumber = int(3000*2*0.3*0.3)
None
degrees.append(1)
degrees.append(1)
SVMMode = 'all'
mode = ["svm"]

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

