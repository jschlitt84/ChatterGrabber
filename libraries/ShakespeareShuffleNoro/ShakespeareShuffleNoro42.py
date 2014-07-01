from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['NLTK_Ready_Tweets.csv']
cores = 2
iterations = 3
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro42Score.txt"
index = 42
gen = 0
prefix = ''
None
SVMMode = 'all'
SVMMode = 'ratio'
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(3000*3*0.3*0.3)
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(3000*1*0.3*0.3)
None
SVMMode = 'number'
SVMNumber = int(3000*5*0.7*0.7)
SVMNumber = int(3000*4*0.6*0.6)
SVMNumber = int(3000*2*0.9*0.9)
SVMMode = 'all'
mode = ["decision tree"]
None
SVMNumber = int(3000*3*0.2*0.2)
None
mode = ["decision tree"]

outFile = open(fileName,'w')
cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber}
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

