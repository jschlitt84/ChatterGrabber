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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg8Score.txt"
index = 8
gen = 0
prefix = ''
degrees.append(6)
mode = ["svm"]
SVMMode = 'number'
degrees.append(2)
degrees.append(4)
SVMNumber = int(3000*5*0.1*0.1)
SVMNumber = int(1*1*0.5)
mode = ["max ent"]
degrees.append(4)
mode = ["svm"]
None
mode = ["max ent"]
SVMMode = 'number'
SVMNumber = int(3000*5*0.7*0.7)
mode = ["svm"]
SVMMode = 'ratio'
SVMNumber = int(1*1*0.99)
SVMNumber = int(5*5*0.99)
None
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

