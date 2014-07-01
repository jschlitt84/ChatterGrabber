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
fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro44Score.txt"
index = 44
gen = 0
prefix = ''
SVMMode = 'number'
mode = ["max ent"]
degrees.append(7)
mode = ["svm"]
None
degrees.append(4)
SVMMode = 'number'
degrees.append(6)
SVMNumber = int(3000*4*0.3*0.3)
SVMNumber = int(3000*7*0.5*0.5)
mode = ["svm"]
degrees.append(5)
None
SVMMode = 'ratio'
degrees.append(4)
mode = ["max ent"]
mode = ["svm"]
None
degrees.append(3)
degrees.append(4)

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

