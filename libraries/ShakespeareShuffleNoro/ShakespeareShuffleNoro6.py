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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro6Score.txt"
index = 6
gen = 0
prefix = ''
SVMMode = 'ratio'
SVMNumber = int(3000*3*0.4*0.4)
degrees.append(6)
SVMMode = 'number'
SVMMode = 'number'
SVMNumber = int(3000*6*0.8*0.8)
mode = ["decision tree"]
mode = ["naive bayes"]
SVMMode = 'number'
SVMNumber = int(3000*4*0.4*0.4)
SVMMode = 'all'
SVMNumber = int(3000*4*0.99*0.99)
SVMMode = 'ratio'
mode = ["max ent"]
None
None
SVMMode = 'ratio'
mode = ["decision tree"]
SVMMode = 'number'
None

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

