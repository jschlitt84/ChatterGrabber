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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro24Score.txt"
index = 24
gen = 0
prefix = ''
degrees.append(1)
mode = ["max ent"]
SVMNumber = int(3000*7*0.7*0.7)
None
SVMMode = 'number'
SVMMode = 'all'
degrees.append(2)
SVMMode = 'all'
SVMNumber = int(3000*2*0.5*0.5)
SVMNumber = int(3000*7*0.1*0.1)
None
SVMMode = 'number'
SVMMode = 'number'
degrees.append(2)
None
mode = ["naive bayes"]
degrees.append(4)
degrees.append(2)
SVMNumber = int(3000*3*0.9*0.9)
degrees.append(6)

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

