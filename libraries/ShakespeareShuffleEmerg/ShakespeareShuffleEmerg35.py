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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg35Score.txt"
index = 35
gen = 7
prefix = ''
SVMMode = 'number'
degrees.append(6)
SVMNumber = int(3000*3*0.4*0.4)
degrees.append(4)
SVMNumber = int(7*7*0.5)
degrees.append(2)
mode = ["max ent"]
None
SVMMode = 'all'
None
SVMMode = 'number'
SVMMode = 'number'
mode = ["naive bayes"]
degrees.append(7)
mode = ["naive bayes"]
SVMNumber = int(3000*5*0.3*0.3)
degrees.append(5)
SVMMode = 'ratio'
SVMNumber = int(4*4*0.3)
SVMMode = 'all'

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

