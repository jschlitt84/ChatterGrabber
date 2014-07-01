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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro11Score.txt"
index = 11
gen = 0
prefix = ''
degrees.append(7)
None
degrees.append(4)
SVMMode = 'number'
None
None
SVMNumber = int(3000*5*0.5*0.5)
None
degrees.append(5)
SVMNumber = int(3000*6*0.2*0.2)
SVMNumber = int(3000*1*0.6*0.6)
None
None
None
SVMMode = 'number'
degrees.append(7)
None
None
mode = ["svm"]
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

