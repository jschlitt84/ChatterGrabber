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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro29Score.txt"
index = 29
gen = 0
prefix = ''
SVMNumber = int(3000*7*0.8*0.8)
degrees.append(5)
SVMNumber = int(3000*2*0.4*0.4)
None
SVMMode = 'number'
SVMMode = 'all'
degrees.append(1)
None
SVMMode = 'number'
None
None
mode = ["svm"]
SVMMode = 'ratio'
None
None
SVMMode = 'ratio'
SVMMode = 'all'
degrees.append(4)
None
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

