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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro20Score.txt"
index = 20
gen = 0
prefix = ''
SVMMode = 'number'
SVMNumber = int(3000*6*0.7*0.7)
mode = ["naive bayes"]
None
degrees.append(1)
SVMNumber = int(3000*5*0.8*0.8)
None
SVMMode = 'all'
SVMNumber = int(3000*2*0.7*0.7)
SVMNumber = int(3000*2*0.4*0.4)
SVMMode = 'all'
None
SVMNumber = int(3000*1*0.1*0.1)
degrees.append(6)
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.99*0.99)
SVMNumber = int(3000*3*0.8*0.8)
SVMMode = 'all'
mode = ["max ent"]
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

