import sys
from TweetMatch import *
from os import getcwd, mkdir, path
from copy import deepcopy

stops = 20

inDir = getcwd().replace('libraries','nlpTrainers')
outDir = getcwd().replace('libraries','optimizeScores')
if 'nlpTrainers' not in inDir:
    inDir += '/nlpTrainers'
if 'optimizeScores' not in outDir:
    outDir += '/optimizeScores'
    
if not path.exists(outDir):
    mkdir(outDir)

sweep = False

if len(sys.argv) > 1:
	if sys.argv[1] == '-s':
		sweep = True
		sys.argv = sys.argv[1:]
		sweepRange = [value/float(stops) for value in range(1,stops)]
		print "SweepRange:", sweepRange
	files = sys.argv[1:]
	print "Running files:", files
else:
	files = ["lymeScores.csv","EmergNLTKScoring.csv","GunTrackerNLTK.csv"]
	records = open('OptimizeScores.txt','w')
	records.write('\n\nNEW OPTIMIZATION RUN\n\n')
	records.close()

#degrees = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[2,3,4],[1,3,4],[1,2,3],[1,2,3,4]]
degrees = [[1],[2],[3],[4],[5]]
modes = ['naive bayes','max ent']

files = [inDir+'/'+inFile for inFile in files]

#sweepRange = [0.05]

for inFile in files:
    outPut = []
    loaded = pd.read_csv(inFile)
    for pos in loaded.index:
        outPut.append({'text': loaded[textColumn][pos], 'category': loaded[categoryColumn][pos]})        
    classifications = set()
    for entry in outPut:
        classifications.add(str(entry['category']))
        
    catCols = ""
    colHeads = sorted(list(classifications))
    for category in colHeads:
        catCols += category+'-sens,'+category+'-spec,'
        
    for mode in modes:
        if mode ==  "max ent":
            degreesTemp = [[1],[2]]
        else:
            degreesTemp = degrees
        for degree in degreesTemp:
            
            if sweep:
                textMode = mode + '.' + str(degree)
                sweepFile = inFile.replace('.csv','.'+textMode+'.csv').replace('nlpTrainers','optimizeScores')
                sweepOut = open(sweepFile,'w')
                sweepOut.write("percent,count,accuracy,stdDev,"+catCols+"\n")
                sweepOut.close()
                for x in sweepRange:
                    accuracy,std,truePercent,count,sensScores,specScores = evalAccuracy(mode,degree,x,deepcopy(classifications),outPut)
                    sweepOut = open(sweepFile,'a+b')
                    summary = "Trainer: %s    Percent: %s    Mode: %s    Degrees: %s    Accuracy: %s    StdDev: %s" % (inFile,truePercent,mode,degree,str(accuracy)[0:5], str(std)[0:3])
                    print '\033[1m\n'+'\033[91m'+summary+'\033[0m'
                    sweepOut.write("%s,%s,%s,%s," % (truePercent,count,accuracy,std))
                    for category in colHeads:
                        sweepOut.write(str(sensScores[category])+', ')
                        sweepOut.write(str(specScores[category])+', ')
                    sweepOut.write('\n')
                    sweepOut.close()
            else:
                accuracy,std,truePercent,count,sensScores,specScores = evalAccuracy(mode,degree,1,deepcopy(classifications),outPut)
                summary = "Trainer: %s    Mode: %s    Degrees: %s    Accuracy: %s    StdDev: %s" % (inFile,mode,degree,str(accuracy)[0:5], str(std)[0:3])
                print '\033[1m\n'+'\033[91m'+summary+'\033[0m'
                records = open('OptimizeScores.txt','a+b')
                records.write('\t'+summary+'\n')
                records.close()
