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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg28Score.txt"
index = 28
gen = 0
prefix = ''
mode = ["naive bayes"]
None
None
mode = ["naive bayes"]
SVMNumber = int(7*7*0.9)
SVMNumber = int(4*4*0.7)
mode = ["naive bayes"]
SVMNumber = int(3000*7*0.1*0.1)
degrees.append(2)
SVMMode = 'ratio'
SVMMode = 'number'
SVMMode = 'ratio'
SVMMode = 'number'
degrees.append(4)
mode = ["max ent"]
SVMNumber = int(5*5*0.8)
None
degrees.append(7)
SVMMode = 'all'
SVMNumber = int(6*6*0.7)

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

