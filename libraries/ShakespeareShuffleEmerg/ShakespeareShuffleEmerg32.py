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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg32Score.txt"
index = 32
gen = 0
prefix = ''
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.8*0.8)
None
SVMNumber = int(3*3*0.6)
SVMNumber = int(2*2*0.8)
mode = ["max ent"]
SVMNumber = int(7*7*0.7)
SVMMode = 'number'
SVMNumber = int(3000*2*0.5*0.5)
None
SVMMode = 'all'
mode = ["naive bayes"]
SVMMode = 'all'
SVMNumber = int(3000*3*0.7*0.7)
degrees.append(2)
None
None
SVMMode = 'number'
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.3*0.3)

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

