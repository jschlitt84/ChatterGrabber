import sys
from TweetMatch import *
from os import getcwd, mkdir, path
from copy import deepcopy
from pandas import read_csv


def getArgs(flag,listed):
    searchText = '-'+flag+'='
    for pos in range(len(listed)):
        if listed[pos].startswith(searchText):
            return listed.pop(pos).replace(searchText,'')
    return 'null'


inDir = getcwd().replace('libraries','nlpTrainers')
outDir = getcwd().replace('libraries','optimizeScores')
if 'nlpTrainers' not in inDir:
    inDir += '/nlpTrainers'
if 'optimizeScores' not in outDir:
    outDir += '/optimizeScores'
    
    
if not path.exists(outDir):
    mkdir(outDir)


stops = 20
iterations = 5
cores = 3
getSweep = False
sweepRange = [.90]
degrees = [[1],[2],[3],[4],[5]]
call = 'default'
prefix = ''
modes = ['naive bayes','max ent']
cfg = dict()


args = list(set(sys.argv[1:]))


iterArg = getArgs('i',args)
if iterArg != 'null':
    iterations = int(iterArg) 

callArg = getArgs('c',args)
if callArg != 'null':
    call = callArg
    
prefixArg = getArgs('p',args)
if prefixArg != 'null':
    prefix = prefixArg
    
coresArg = getArgs('x',args)
if coresArg != 'null':
    cores = int(coresArg)
    
stopArg = getArgs('s',args)
if stopArg != 'null':
    if not stopArg.startswith('['):
        stops = int(stopArg)
        sweepRange = [value/float(stops) for value in range(1,stops)]
    else:
        sweepRange = eval(stopArg)  
    
degreeArg = getArgs('d',args)
if degreeArg != 'null':
    if not degreeArg.startswith('['):
        degrees = [[int(degreeArg)]]
    else:
        degrees = eval(degreeArg)
    
modeArg = getArgs('m',args)
if modeArg != 'null':
    if not modeArg.startswith('['):
        modes = [modeArg]
    else:
        modes = eval(modeArg)

cfgArg = getArgs('cfg',args)
if cfgArg != 'null':
    cfgTemp = eval(cfgArg)
    if type(cfgTemp) is dict:
        cfg = cfgTemp


print "\nRunning files", args, "with degrees", degrees, "and modes", modes, "over sweep range", sweepRange, "for", iterations, "iterations.\n"

				
files = [inDir+'/'+inFile for inFile in args]


for inFile in files:
    outPut = []
    loaded = read_csv(inFile)
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
        for degree in degrees:
            textMode = mode + '.' + str(degree)
            sweepFile = inFile.replace('.csv','.'+textMode+'.csv').replace('nlpTrainers','optimizeScores')
            sweepOut = open(sweepFile,'w')
            sweepOut.write("percent,count,accuracy,stdDev,"+catCols+"\n")
            sweepOut.close()
            for x in sweepRange:
                accuracy,std,truePercent,count,sensScores,specScores = evalAccuracy(mode,degree,iterations,x,cores,deepcopy(classifications),outPut,cfg)
                sweepOut = open(sweepFile,'a+b')
                summary = "Trainer: %s    Percent: %s    Mode: %s    Degrees: %s    Accuracy: %s    StdDev: %s" % (inFile,truePercent,mode,degree,str(accuracy)[0:5], str(std)[0:3])
                print '\033[1m\n'+'\033[91m'+summary+'\033[0m'
                sweepOut.write("%s,%s,%s,%s," % (truePercent,count,accuracy,std))
                for category in colHeads:
                    sweepOut.write(str(sensScores[category])+', ')
                    sweepOut.write(str(specScores[category])+', ')
                sweepOut.write('\n')
                sweepOut.close()