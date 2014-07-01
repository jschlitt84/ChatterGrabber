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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg31Score.txt"
index = 31
gen = 0
prefix = ''
None
SVMMode = 'ratio'
degrees.append(7)
degrees.append(4)
SVMNumber = int(3000*2*0.7*0.7)
SVMMode = 'all'
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(2*2*0.5)
None
SVMNumber = int(3000*3*0.3*0.3)
None
degrees.append(2)
SVMNumber = int(5*5*0.5)
SVMNumber = int(3000*5*0.6*0.6)
SVMNumber = int(1*1*0.4)
SVMMode = 'number'
degrees.append(5)
SVMNumber = int(3000*4*0.4*0.4)
SVMNumber = int(1*1*0.5)

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

