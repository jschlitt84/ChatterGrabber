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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg38Score.txt"
index = 38
gen = 0
prefix = ''
degrees.append(1)
SVMNumber = int(2*2*0.99)
SVMNumber = int(1*1*0.8)
None
SVMNumber = int(4*4*0.99)
degrees.append(1)
SVMMode = 'ratio'
mode = ["naive bayes"]
SVMMode = 'all'
None
SVMNumber = int(3000*6*0.4*0.4)
SVMNumber = int(4*4*0.8)
SVMMode = 'number'
degrees.append(4)
SVMNumber = int(3000*7*0.9*0.9)
degrees.append(4)
SVMNumber = int(2*2*0.4)
None
mode = ["naive bayes"]
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

