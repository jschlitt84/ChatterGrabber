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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro14Score.txt"
index = 14
gen = 0
prefix = ''
None
None
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.1*0.1)
None
degrees.append(3)
SVMMode = 'all'
SVMNumber = int(3000*2*0.5*0.5)
mode = ["naive bayes"]
None
degrees.append(6)
SVMMode = 'number'
None
SVMNumber = int(3000*5*0.5*0.5)
None
None
mode = ["max ent"]
SVMMode = 'number'
mode = ["decision tree"]
mode = ["max ent"]

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

