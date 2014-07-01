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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg36Score.txt"
index = 36
gen = 0
prefix = ''
None
degrees.append(3)
SVMNumber = int(3000*6*0.6*0.6)
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.4*0.4)
degrees.append(1)
None
degrees.append(6)
SVMMode = 'all'
SVMMode = 'ratio'
SVMNumber = int(3000*4*0.2*0.2)
SVMNumber = int(6*6*0.8)
SVMMode = 'number'
None
SVMNumber = int(3000*5*0.7*0.7)
None
mode = ["max ent"]
None
mode = ["naive bayes"]
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

