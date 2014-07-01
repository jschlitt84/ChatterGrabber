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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro1Score.txt"
index = 1
gen = 0
prefix = ''
SVMMode = 'all'
SVMNumber = int(3000*7*0.99*0.99)
None
mode = ["max ent"]
degrees.append(4)
SVMNumber = int(3000*2*0.99*0.99)
degrees.append(6)
None
SVMNumber = int(3000*4*0.9*0.9)
mode = ["svm"]
SVMNumber = int(3000*1*0.7*0.7)
None
SVMNumber = int(3000*6*0.5*0.5)
degrees.append(1)
SVMMode = 'ratio'
mode = ["max ent"]
SVMMode = 'ratio'
degrees.append(4)
degrees.append(2)
SVMMode = 'all'

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

