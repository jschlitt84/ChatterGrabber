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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg29Score.txt"
index = 29
gen = 2
prefix = ''
SVMMode = 'ratio'
degrees.append(6)
None
SVMNumber = int(3000*2*0.6*0.6)
SVMNumber = int(7*7*0.5)
SVMNumber = int(3000*7*0.5*0.5)
SVMNumber = int(3000*7*0.2*0.2)
SVMNumber = int(3000*1*0.99*0.99)
SVMNumber = int(3000*3*0.5*0.5)
degrees.append(3)
degrees.append(4)
SVMNumber = int(3000*3*0.6*0.6)
None
SVMNumber = int(3000*4*0.99*0.99)
mode = ["naive bayes"]
SVMNumber = int(2*2*0.2)
degrees.append(6)
SVMMode = 'ratio'
None
None

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

