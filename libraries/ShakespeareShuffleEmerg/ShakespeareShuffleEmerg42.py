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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg42Score.txt"
index = 42
gen = 5
prefix = ''
SVMMode = 'all'
SVMMode = 'all'
SVMNumber = int(3*3*0.1)
SVMNumber = int(3000*2*0.6*0.6)
SVMNumber = int(3*3*0.2)
SVMNumber = int(2*2*0.5)
None
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.5*0.5)
SVMNumber = int(7*7*0.1)
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.9*0.9)
mode = ["max ent"]
SVMMode = 'all'
SVMNumber = int(3000*7*0.9*0.9)
SVMNumber = int(3000*7*0.7*0.7)
degrees.append(2)
degrees.append(4)
SVMNumber = int(3000*6*0.1*0.1)
SVMNumber = int(3000*3*0.8*0.8)

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

