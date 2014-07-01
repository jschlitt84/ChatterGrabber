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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg23Score.txt"
index = 23
gen = 1
prefix = ''
None
SVMMode = 'ratio'
None
SVMMode = 'number'
SVMNumber = int(3000*2*0.7*0.7)
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(3000*2*0.5*0.5)
None
SVMMode = 'all'
None
degrees.append(2)
SVMNumber = int(3000*3*0.7*0.7)
SVMNumber = int(3000*5*0.6*0.6)
None
None
SVMNumber = int(3000*3*0.8*0.8)
mode = ["naive bayes"]
degrees.append(1)

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

