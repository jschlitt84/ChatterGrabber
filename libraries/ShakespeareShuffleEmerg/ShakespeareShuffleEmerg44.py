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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg44Score.txt"
index = 44
gen = 7
prefix = ''
SVMMode = 'number'
mode = ["svm"]
mode = ["naive bayes"]
mode = ["max ent"]
degrees.append(1)
mode = ["svm"]
degrees.append(1)
SVMNumber = int(5*5*0.4)
SVMNumber = int(3000*7*0.9*0.9)
SVMNumber = int(5*5*0.2)
mode = ["svm"]
SVMNumber = int(4*4*0.1)
None
mode = ["max ent"]
SVMNumber = int(2*2*0.8)
mode = ["max ent"]
None
degrees.append(4)
degrees.append(5)
SVMNumber = int(4*4*0.99)

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

