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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg21Score.txt"
index = 21
gen = 0
prefix = ''
SVMNumber = int(7*7*0.4)
mode = ["naive bayes"]
None
mode = ["max ent"]
None
SVMNumber = int(3000*3*0.5*0.5)
SVMMode = 'ratio'
degrees.append(3)
SVMNumber = int(3000*7*0.5*0.5)
None
SVMNumber = int(3000*5*0.99*0.99)
mode = ["naive bayes"]
mode = ["svm"]
SVMNumber = int(1*1*0.4)
SVMNumber = int(4*4*0.9)
SVMNumber = int(7*7*0.9)
SVMNumber = int(1*1*0.3)
mode = ["svm"]
SVMMode = 'all'
mode = ["naive bayes"]

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

