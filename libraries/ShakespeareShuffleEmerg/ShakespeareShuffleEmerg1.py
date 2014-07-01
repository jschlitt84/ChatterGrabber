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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg1Score.txt"
index = 1
gen = 0
prefix = ''
mode = ["max ent"]
SVMNumber = int(3000*6*0.8*0.8)
degrees.append(6)
SVMNumber = int(3000*6*0.99*0.99)
degrees.append(3)
mode = ["svm"]
SVMNumber = int(7*7*0.7)
SVMMode = 'number'
degrees.append(3)
None
None
mode = ["naive bayes"]
degrees.append(1)
SVMNumber = int(3000*3*0.7*0.7)
degrees.append(2)
SVMNumber = int(3000*4*0.6*0.6)
degrees.append(4)
SVMMode = 'number'
SVMNumber = int(3000*2*0.7*0.7)
SVMMode = 'ratio'

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

