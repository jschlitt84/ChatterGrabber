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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro8Score.txt"
index = 8
gen = 0
prefix = ''
SVMNumber = int(3000*7*0.5*0.5)
mode = ["max ent"]
SVMNumber = int(3000*7*0.7*0.7)
SVMNumber = int(3000*1*0.5*0.5)
SVMMode = 'number'
mode = ["svm"]
mode = ["svm"]
mode = ["max ent"]
SVMNumber = int(3000*1*0.2*0.2)
degrees.append(1)
None
SVMNumber = int(3000*6*0.3*0.3)
SVMMode = 'ratio'
SVMNumber = int(3000*7*0.4*0.4)
SVMMode = 'number'
None
None
SVMMode = 'number'
mode = ["naive bayes"]
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

