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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro18Score.txt"
index = 18
gen = 0
prefix = ''
None
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(7)
mode = ["naive bayes"]
None
mode = ["naive bayes"]
mode = ["naive bayes"]
None
degrees.append(1)
degrees.append(2)
SVMNumber = int(3000*2*0.6*0.6)
SVMNumber = int(3000*7*0.99*0.99)
degrees.append(7)
None
degrees.append(4)
mode = ["max ent"]
mode = ["naive bayes"]
SVMNumber = int(3000*3*0.6*0.6)
mode = ["max ent"]
SVMMode = 'number'

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

