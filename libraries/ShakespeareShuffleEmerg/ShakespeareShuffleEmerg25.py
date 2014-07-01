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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg25Score.txt"
index = 25
gen = 0
prefix = ''
None
degrees.append(6)
degrees.append(3)
SVMNumber = int(6*6*0.8)
SVMNumber = int(3*3*0.2)
SVMNumber = int(3000*7*0.5*0.5)
degrees.append(4)
SVMNumber = int(3000*1*0.99*0.99)
SVMMode = 'number'
mode = ["svm"]
degrees.append(4)
SVMNumber = int(3000*3*0.6*0.6)
degrees.append(5)
SVMNumber = int(3*3*0.3)
mode = ["naive bayes"]
SVMMode = 'number'
degrees.append(2)
mode = ["max ent"]
SVMNumber = int(3000*6*0.1*0.1)
degrees.append(6)

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

