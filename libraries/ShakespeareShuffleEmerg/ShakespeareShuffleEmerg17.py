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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg17Score.txt"
index = 17
gen = 0
prefix = ''
SVMNumber = int(3000*6*0.99*0.99)
mode = ["max ent"]
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.5*0.5)
SVMNumber = int(2*2*0.7)
degrees.append(3)
SVMNumber = int(2*2*0.5)
mode = ["max ent"]
SVMNumber = int(4*4*0.6)
None
degrees.append(3)
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*7*0.2*0.2)
degrees.append(2)
None
mode = ["max ent"]
mode = ["svm"]
SVMNumber = int(3000*4*0.99*0.99)
SVMNumber = int(3000*2*0.9*0.9)

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

