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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro39Score.txt"
index = 39
gen = 0
prefix = ''
mode = ["naive bayes"]
degrees.append(5)
mode = ["decision tree"]
None
degrees.append(4)
SVMNumber = int(3000*1*0.99*0.99)
SVMMode = 'number'
SVMMode = 'all'
degrees.append(4)
None
degrees.append(5)
SVMNumber = int(3000*6*0.4*0.4)
SVMNumber = int(3000*1*0.3*0.3)
None
mode = ["max ent"]
degrees.append(1)
degrees.append(1)
degrees.append(1)
SVMNumber = int(3000*3*0.1*0.1)
degrees.append(2)

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

