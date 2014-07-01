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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro4Score.txt"
index = 4
gen = 0
prefix = ''
mode = ["svm"]
None
degrees.append(4)
mode = ["decision tree"]
degrees.append(6)
degrees.append(4)
SVMMode = 'ratio'
degrees.append(1)
mode = ["svm"]
degrees.append(1)
SVMMode = 'ratio'
degrees.append(2)
mode = ["max ent"]
mode = ["naive bayes"]
degrees.append(1)
SVMNumber = int(3000*2*0.2*0.2)
mode = ["max ent"]
SVMNumber = int(3000*1*0.2*0.2)
SVMNumber = int(3000*5*0.1*0.1)
mode = ["svm"]

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

