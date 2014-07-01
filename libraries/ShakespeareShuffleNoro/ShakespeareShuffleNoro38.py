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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro38Score.txt"
index = 38
gen = 0
prefix = ''
None
degrees.append(2)
mode = ["svm"]
SVMNumber = int(3000*6*0.1*0.1)
None
SVMNumber = int(3000*3*0.6*0.6)
mode = ["max ent"]
SVMNumber = int(3000*7*0.8*0.8)
None
None
SVMNumber = int(3000*6*0.3*0.3)
SVMNumber = int(3000*4*0.6*0.6)
SVMNumber = int(3000*2*0.9*0.9)
None
mode = ["naive bayes"]
mode = ["max ent"]
SVMNumber = int(3000*1*0.1*0.1)
None
SVMNumber = int(3000*2*0.3*0.3)
SVMMode = 'ratio'

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

