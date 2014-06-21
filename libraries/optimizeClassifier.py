from TweetMatch import *
import sys

directory = '/Users/jamesschlitt/ChatterGrabber/nlpTrainers/'
#directory = '/home/jschlitt/Dropbox/ChatterGrabberPortable/nlpTrainers/'

sweep = False

if len(sys.argv) > 1:
	if sys.argv[1] == '-s':
		sweep = True
		sys.argv = sys.argv[1:]
		sweepRange = [value/50. for value in range(1,50)]
	files = sys.argv[1:]
	print "Running files:", files
else:
	files = ["lymeScores.csv","EmergNLTKScoring.csv","GunTrackerNLTK.csv"]
	records = open('OptimizeScores.txt','w')
	records.write('\n\nNEW OPTIMIZATION RUN\n\n')
	records.close()

degrees = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[2,3,4],[1,3,4],[1,2,3],[1,2,3,4]]
#modes = ['naive bayes','max ent']
modes = ['naive bayes','max ent']

for inFile in files:
    for mode in modes:
        if mode ==  "max ent":
            degreesTemp = [[1]]
        else:
            degreesTemp = degrees
        for degree in degreesTemp:
            if sweep:
                textMode = mode + '.' + str(degree)
                sweepFile = inFile.replace('.csv',textMode+'.csv')
                sweepOut = open(sweepFile,'w')
                sweepOut.write("percent,accuracy,stdDev,\n")
                sweepOut.close()
                for x in sweepRange:
                    accuracy,std = evalAccuracy(directory+inFile,mode,degree,x)
                    sweepOut = open(sweepFile,'a+b')
                    summary = "Trainer: %s    Percent: %s    Mode: %s    Degrees: %s    Accuracy: %s    StdDev: %s" % (inFile,x,mode,degree,str(accuracy)[0:5], str(std)[0:3])
                    print '\033[1m\n'+'\033[91m'+summary+'\033[0m'
                    sweepOut.write("%s,%s,%s,\n" % (x,accuracy,std))
                    sweepOut.close()
            else:
                accuracy,std = evalAccuracy(directory+inFile,mode,degree,1)
                summary = "Trainer: %s    Mode: %s    Degrees: %s    Accuracy: %s    StdDev: %s" % (inFile,mode,degree,str(accuracy)[0:5], str(std)[0:3])
                print '\033[1m\n'+'\033[91m'+summary+'\033[0m'
                records = open('OptimizeScores.txt','a+b')
                records.write('\t'+summary+'\n')
                records.close()
