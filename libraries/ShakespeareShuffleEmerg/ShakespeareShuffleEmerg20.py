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
fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg20Score.txt"
index = 20
gen = 6
prefix = ''
SVMMode = 'ratio'
None
None
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.8*0.8)
SVMMode = 'number'
SVMMode = 'number'
mode = ["max ent"]
SVMNumber = int(3000*2*0.99*0.99)
SVMNumber = int(3000*7*0.99*0.99)
SVMNumber = int(3000*1*0.9*0.9)
degrees.append(5)
SVMNumber = int(7*7*0.6)
mode = ["naive bayes"]
SVMNumber = int(3*3*0.8)
SVMNumber = int(3000*6*0.4*0.4)
SVMNumber = int(3000*1*0.7*0.7)
mode = ["max ent"]
SVMNumber = int(3000*2*0.9*0.9)
mode = ["naive bayes"]

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

