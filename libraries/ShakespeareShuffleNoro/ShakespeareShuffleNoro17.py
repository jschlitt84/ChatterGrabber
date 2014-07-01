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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro17Score.txt"
index = 17
gen = 0
prefix = ''
mode = ["naive bayes"]
degrees.append(1)
degrees.append(4)
degrees.append(4)
degrees.append(7)
SVMMode = 'number'
degrees.append(1)
None
SVMMode = 'all'
degrees.append(6)
SVMNumber = int(3000*1*0.5*0.5)
SVMMode = 'number'
degrees.append(1)
mode = ["naive bayes"]
SVMNumber = int(3000*4*0.3*0.3)
None
None
None
SVMMode = 'all'
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

