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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro30Score.txt"
index = 30
gen = 0
prefix = ''
mode = ["decision tree"]
mode = ["svm"]
SVMNumber = int(3000*5*0.3*0.3)
degrees.append(4)
SVMMode = 'all'
SVMMode = 'all'
degrees.append(5)
SVMMode = 'number'
None
SVMMode = 'ratio'
degrees.append(5)
SVMNumber = int(3000*1*0.3*0.3)
SVMMode = 'number'
None
SVMMode = 'number'
degrees.append(4)
mode = ["max ent"]
degrees.append(4)
SVMMode = 'number'
degrees.append(7)

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

