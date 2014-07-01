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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg33Score.txt"
index = 33
gen = 0
prefix = ''
degrees.append(5)
SVMNumber = int(5*5*0.99)
SVMNumber = int(5*5*0.6)
None
degrees.append(2)
SVMNumber = int(1*1*0.99)
None
SVMNumber = int(3000*4*0.7*0.7)
None
mode = ["max ent"]
SVMMode = 'number'
None
SVMNumber = int(3*3*0.8)
None
degrees.append(1)
degrees.append(6)
None
degrees.append(4)
mode = ["naive bayes"]
SVMNumber = int(1*1*0.7)

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

