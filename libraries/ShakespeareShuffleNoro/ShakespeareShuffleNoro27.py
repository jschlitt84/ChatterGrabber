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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro27Score.txt"
index = 27
gen = 0
prefix = ''
SVMMode = 'number'
degrees.append(5)
degrees.append(7)
SVMMode = 'number'
mode = ["max ent"]
mode = ["decision tree"]
degrees.append(5)
degrees.append(5)
degrees.append(3)
SVMMode = 'all'
SVMMode = 'number'
None
SVMNumber = int(3000*6*0.99*0.99)
SVMMode = 'number'
degrees.append(1)
mode = ["decision tree"]
SVMNumber = int(3000*4*0.2*0.2)
degrees.append(6)
None
None

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

