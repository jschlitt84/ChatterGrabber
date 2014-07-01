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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro35Score.txt"
index = 35
gen = 0
prefix = ''
None
None
degrees.append(3)
None
degrees.append(4)
None
SVMNumber = int(3000*4*0.3*0.3)
degrees.append(2)
mode = ["naive bayes"]
degrees.append(2)
SVMMode = 'number'
SVMMode = 'all'
None
SVMMode = 'all'
degrees.append(5)
mode = ["naive bayes"]
degrees.append(5)
SVMMode = 'all'
SVMNumber = int(3000*1*0.8*0.8)
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

