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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro23Score.txt"
index = 23
gen = 0
prefix = ''
degrees.append(2)
degrees.append(1)
SVMMode = 'number'
mode = ["naive bayes"]
SVMNumber = int(3000*6*0.99*0.99)
SVMNumber = int(3000*4*0.99*0.99)
SVMMode = 'number'
SVMMode = 'number'
SVMMode = 'all'
SVMNumber = int(3000*2*0.99*0.99)
mode = ["max ent"]
mode = ["naive bayes"]
degrees.append(5)
mode = ["decision tree"]
SVMNumber = int(3000*5*0.2*0.2)
degrees.append(1)
mode = ["max ent"]
SVMNumber = int(3000*2*0.5*0.5)
SVMNumber = int(3000*5*0.6*0.6)
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

