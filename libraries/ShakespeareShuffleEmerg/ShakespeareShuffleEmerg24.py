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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg24Score.txt"
index = 24
gen = 0
prefix = ''
degrees.append(2)
SVMNumber = int(3000*1*0.4*0.4)
SVMNumber = int(5*5*0.1)
SVMNumber = int(7*7*0.1)
SVMMode = 'all'
degrees.append(2)
mode = ["max ent"]
SVMMode = 'ratio'
mode = ["naive bayes"]
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.3*0.3)
degrees.append(3)
None
SVMNumber = int(3000*1*0.99*0.99)
SVMMode = 'number'
SVMNumber = int(3000*1*0.1*0.1)
degrees.append(3)
SVMMode = 'number'
SVMNumber = int(3*3*0.2)
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

