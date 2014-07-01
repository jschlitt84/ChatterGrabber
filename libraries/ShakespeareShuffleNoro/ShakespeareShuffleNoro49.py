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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro49Score.txt"
index = 49
gen = 0
prefix = ''
None
SVMMode = 'ratio'
mode = ["max ent"]
SVMNumber = int(3000*7*0.2*0.2)
mode = ["decision tree"]
mode = ["max ent"]
degrees.append(7)
mode = ["decision tree"]
SVMMode = 'ratio'
SVMNumber = int(3000*6*0.6*0.6)
SVMNumber = int(3000*1*0.5*0.5)
mode = ["naive bayes"]
SVMMode = 'ratio'
SVMMode = 'ratio'
mode = ["naive bayes"]
mode = ["decision tree"]
None
mode = ["naive bayes"]
SVMMode = 'number'
SVMNumber = int(3000*3*0.7*0.7)

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

