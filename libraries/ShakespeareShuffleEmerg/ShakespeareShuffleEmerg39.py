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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg39Score.txt"
index = 39
gen = 7
prefix = ''
SVMNumber = int(3000*1*0.4*0.4)
mode = ["naive bayes"]
None
SVMMode = 'number'
degrees.append(4)
mode = ["naive bayes"]
SVMMode = 'ratio'
mode = ["svm"]
SVMNumber = int(2*2*0.6)
degrees.append(7)
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(5*5*0.99)
mode = ["naive bayes"]
SVMMode = 'ratio'
mode = ["naive bayes"]
SVMNumber = int(3*3*0.4)
mode = ["svm"]
SVMNumber = int(3000*1*0.6*0.6)
SVMNumber = int(1*1*0.6)

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

