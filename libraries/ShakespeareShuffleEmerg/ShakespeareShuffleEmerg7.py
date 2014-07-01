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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg7Score.txt"
index = 7
gen = 0
prefix = ''
SVMNumber = int(3000*5*0.99*0.99)
SVMNumber = int(3*3*0.5)
SVMMode = 'ratio'
None
SVMNumber = int(4*4*0.5)
degrees.append(6)
SVMMode = 'number'
SVMNumber = int(4*4*0.8)
mode = ["naive bayes"]
SVMNumber = int(7*7*0.99)
mode = ["max ent"]
degrees.append(7)
degrees.append(5)
degrees.append(6)
SVMMode = 'all'
SVMNumber = int(3000*6*0.99*0.99)
SVMNumber = int(3000*3*0.99*0.99)
SVMNumber = int(3*3*0.5)
SVMNumber = int(3000*4*0.6*0.6)
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

