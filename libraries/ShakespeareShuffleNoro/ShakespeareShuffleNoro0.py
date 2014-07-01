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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro0Score.txt"
index = 0
gen = 0
prefix = ''
SVMMode = 'number'
None
SVMNumber = int(3000*3*0.9*0.9)
SVMMode = 'number'
degrees.append(3)
degrees.append(3)
degrees.append(6)
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(3000*5*0.9*0.9)
None
SVMMode = 'all'
SVMMode = 'all'
SVMMode = 'all'
degrees.append(2)
None
None
None
degrees.append(6)
degrees.append(1)

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

