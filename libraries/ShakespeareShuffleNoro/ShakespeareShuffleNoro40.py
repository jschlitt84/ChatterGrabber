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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro40Score.txt"
index = 40
gen = 0
prefix = ''
mode = ["naive bayes"]
None
None
SVMNumber = int(3000*5*0.5*0.5)
degrees.append(6)
mode = ["max ent"]
None
None
SVMNumber = int(3000*3*0.1*0.1)
SVMNumber = int(3000*6*0.8*0.8)
SVMMode = 'all'
None
mode = ["svm"]
degrees.append(1)
mode = ["svm"]
SVMNumber = int(3000*1*0.9*0.9)
degrees.append(4)
SVMMode = 'ratio'
degrees.append(5)
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

