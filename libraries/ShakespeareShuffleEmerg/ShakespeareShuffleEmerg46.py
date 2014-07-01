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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg46Score.txt"
index = 46
gen = 7
prefix = ''
None
SVMNumber = int(2*2*0.99)
degrees.append(3)
SVMNumber = int(6*6*0.8)
None
SVMMode = 'number'
degrees.append(4)
mode = ["naive bayes"]
SVMMode = 'all'
None
SVMNumber = int(3000*6*0.4*0.4)
SVMNumber = int(3000*3*0.6*0.6)
None
degrees.append(4)
SVMNumber = int(3000*7*0.9*0.9)
SVMMode = 'number'
SVMNumber = int(2*2*0.4)
mode = ["max ent"]
SVMNumber = int(3000*6*0.1*0.1)
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

