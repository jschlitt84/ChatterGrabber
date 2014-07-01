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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro28Score.txt"
index = 28
gen = 0
prefix = ''
mode = ["svm"]
None
degrees.append(3)
None
None
mode = ["max ent"]
SVMNumber = int(3000*3*0.2*0.2)
SVMMode = 'number'
None
SVMNumber = int(3000*7*0.4*0.4)
degrees.append(3)
SVMNumber = int(3000*3*0.3*0.3)
None
degrees.append(3)
mode = ["svm"]
SVMNumber = int(3000*7*0.6*0.6)
SVMMode = 'number'
SVMMode = 'ratio'
degrees.append(6)
mode = ["naive bayes"]

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

