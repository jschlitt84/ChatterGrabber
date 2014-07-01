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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg27Score.txt"
index = 27
gen = 2
prefix = ''
SVMMode = 'ratio'
SVMMode = 'all'
SVMMode = 'number'
mode = ["svm"]
degrees.append(4)
None
None
None
mode = ["max ent"]
mode = ["svm"]
degrees.append(4)
SVMNumber = int(3000*3*0.6*0.6)
mode = ["max ent"]
SVMMode = 'ratio'
None
SVMNumber = int(3000*7*0.7*0.7)
degrees.append(2)
SVMNumber = int(1*1*0.5)
SVMNumber = int(1*1*0.8)
SVMNumber = int(3000*2*0.6*0.6)

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

