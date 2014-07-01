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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro13Score.txt"
index = 13
gen = 0
prefix = ''
None
None
mode = ["decision tree"]
SVMMode = 'number'
SVMMode = 'number'
SVMNumber = int(3000*1*0.8*0.8)
SVMNumber = int(3000*1*0.3*0.3)
None
mode = ["svm"]
None
SVMNumber = int(3000*7*0.99*0.99)
None
None
degrees.append(6)
degrees.append(6)
mode = ["svm"]
None
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(3000*6*0.9*0.9)

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

