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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg45Score.txt"
index = 45
gen = 6
prefix = ''
degrees.append(5)
SVMNumber = int(3*3*0.5)
degrees.append(7)
degrees.append(6)
SVMMode = 'all'
degrees.append(6)
degrees.append(6)
None
mode = ["naive bayes"]
degrees.append(4)
SVMNumber = int(1*1*0.1)
degrees.append(7)
degrees.append(5)
mode = ["naive bayes"]
SVMNumber = int(3*3*0.2)
SVMMode = 'ratio'
degrees.append(1)
SVMNumber = int(3*3*0.5)
SVMNumber = int(3000*7*0.6*0.6)
mode = ["max ent"]

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

