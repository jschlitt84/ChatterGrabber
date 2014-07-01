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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg11Score.txt"
index = 11
gen = 0
prefix = ''
SVMMode = 'all'
SVMMode = 'all'
SVMNumber = int(3*3*0.1)
SVMNumber = int(3000*2*0.8*0.8)
SVMMode = 'all'
None
None
None
SVMNumber = int(1*1*0.99)
SVMNumber = int(7*7*0.1)
None
SVMNumber = int(3000*7*0.3*0.3)
mode = ["max ent"]
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(3000*7*0.7*0.7)
degrees.append(2)
SVMNumber = int(7*7*0.9)
SVMNumber = int(1*1*0.3)
degrees.append(4)

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

