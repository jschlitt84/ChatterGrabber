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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg3Score.txt"
index = 3
gen = 0
prefix = ''
None
degrees.append(6)
SVMNumber = int(3000*4*0.4*0.4)
SVMMode = 'number'
SVMNumber = int(4*4*0.5)
SVMNumber = int(3000*3*0.6*0.6)
SVMMode = 'ratio'
SVMMode = 'ratio'
SVMNumber = int(5*5*0.7)
degrees.append(1)
degrees.append(3)
SVMNumber = int(5*5*0.99)
degrees.append(4)
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(7*7*0.6)
degrees.append(1)
None
SVMNumber = int(5*5*0.7)
None

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

