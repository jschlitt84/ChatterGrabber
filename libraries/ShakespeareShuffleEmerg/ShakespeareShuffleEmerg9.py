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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg9Score.txt"
index = 9
gen = 4
prefix = ''
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.7*0.7)
SVMMode = 'ratio'
SVMNumber = int(7*7*0.99)
SVMNumber = int(3000*3*0.2*0.2)
None
mode = ["max ent"]
None
SVMMode = 'ratio'
SVMMode = 'all'
degrees.append(7)
degrees.append(7)
SVMMode = 'all'
SVMNumber = int(3000*3*0.3*0.3)
mode = ["naive bayes"]
SVMNumber = int(2*2*0.9)
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMNumber = int(2*2*0.1)
SVMNumber = int(4*4*0.8)

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

