import random
import sys, os
import subprocess
import time
import select
from math import sqrt

def getNumProc(name):
    ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
    processes = ps.split('\n')
    count = 0
    for process in processes:
        if name in process:
            count += 1
    print count, "processes running"
    return count - 1

def adjustError(diversity):
    return ((1-diversity)*4+1)

def fileName(name, number):
    return name + '/' + name + str(number) + '.py'

def scoreName(name, number):
    return name + '/' + name + str(number) + 'Score.txt'
    
def logName(name, number):
    return name + '/' + name + str(number) + 'Log.txt'

def countHidden(fileName):
    scriptIn = open(fileName)
    script = scriptIn.read()
    scriptIn.close()
    return script.count('#')
      
def makeFile(header, code, footer, name, lines, linesOut, scoreOut, number, isOffspring, generation):
    headTemp = header[:]
    headTemp.insert(-1,'fileName = "' + scoreName(name,number) + '"')
    headTemp.insert(-1,'index = ' + str(number))
    headTemp.insert(-1,'gen = ' + str(generation))
    footTemp = footer[:]
    footTemp.insert(0,"\noutFile = open(fileName,'w')")
    outScript = headTemp+ code + footTemp
    outFile = open(fileName(name,number), 'w')
    for item in outScript:
        outFile.write("%s\n" % item)
    outFile.close()    

def makeCode(word1,word2,word3,word4,word5,code):
    line = random.choice(code)
    if len(word1) > 0:
        line = line.replace('@1',random.choice(word1))
    if len(word2) > 0:
        line = line.replace('@2',random.choice(word2))
    if len(word3) > 0:
        line = line.replace('@3',random.choice(word3))
    if len(word4) > 0:
        line = line.replace('@4',random.choice(word4))
    if len(word5) > 0:
        line = line.replace('@5',random.choice(word5))
    return line

def makeLines(word1,word2,word3,word4,word5,code,lines):
    script = []
    for pos in range(lines):
        script.append(makeCode(word1,word2,word3,word4,word5,code))
    return script

def breedScripts(file1,file2,start,end,mateError,word1,word2,word3,word4,word5,code):
    scriptIn = open(file1)
    script1 = scriptIn.readlines()
    scriptIn.close()
    scriptIn = open(file2)
    script2 = scriptIn.readlines()
    scriptIn.close()
    script1 = script1[start-1:-end]
    script2 = script2[start-1:-end]
    for pos in range(len(script1)):
        if random.random()<mateError:
            script1[pos] = makeCode(word1,word2,word3,word4,word5,code)
        elif bool(random.randint(0,1)):
            script1[pos] = script2[pos]
        script1[pos] = script1[pos].replace('\n','')
    return script1
    
def mutateBest(file1,start,end,pointMute,word1,word2,word3,word4,word5,code):
    scriptIn = open(file1)
    script1 = scriptIn.readlines()
    scriptIn.close()
    script1 = script1[start-1:-end]
    for pos in range(len(script1)):
        choice = random.randint(1,3)
        if random.random()<pointMute:
            choice = random.randint(1,3)
            if choice == 1:
                script1[pos] = makeCode(word1,word2,word3,word4,word5,code)
            elif choice == 2:
                del script1[pos]
                script1.append(makeCode(word1,word2,word3,word4,word5,code))
            else:
                del script1[-1]
                script1.insert(pos,makeCode(word1,word2,word3,word4,word5,code))
        script1[pos] = script1[pos].replace('\n','')
    return script1

def main():
        
    try:
        target =  sys.argv[1]
    except:
        target = 'config.txt'
    try:
        if sys.argv[2][0].lower() == 'c':
            carryOn = True
    except:
        carryOn = False
        
        
    configFile = open(target)
       
    name = "pyGeneDefault"
    seeds = 250
    lines = 100
    pointMute = 0.10
    kill = 125
    new = 25
    muteBest = 10
    linesOut = 4
    scoreOut = 4
    increment = 2
    inputDelay = 10
    mateError = 0.01
    rescore = False
    noLoadScore = -99999999
    punishCopies = 100
    scoreToWin = 10000
    gotHeader = False
    gotFooter = False
    gotCode = False
    countOff = False
    replaceWeak = True
    toKeep = []
    
    code = []
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    word5 = []
    header = []
    footer = []
    
    gottaGo = kill+new+muteBest
    extraReplace = 0
    extraKills = 0
    extraMutes = 0
    maxRunning = False
    
    script =  configFile.readlines()
    print "Script:", script
    configFile.close()        
    
    length = len(script)
    pos = 0
    
    while pos < length:
        line = script[pos]
        if not line.startswith('#'):
            if line.startswith("Name = "):
                name = (line.replace('Name = ','').replace('\n','')).replace(' ','')
            elif line.startswith("Number of seeds = "):
                seeds = int(line.replace('Number of seeds = ',''))
            elif line.startswith("Lines per seed = "):
                lines = int(line.replace('Lines per seed = ',''))
            elif line.startswith("Runs per query = "):
                increment = int(line.replace('Runs per query = ','')) 
            elif line.startswith("Query delay = "):
                inputDelay = int(line.replace('Query delay = ',''))   
            elif line.startswith("Point mutation = "): 
                pointMute = int(line.replace('Point mutation = ',''))
            elif line.startswith("Kill"):
                kill = int(line.replace('Kill = ','').replace('\n',''))
            elif line.startswith("New"):
                new = int(line.replace('New = ','').replace('\n',''))
            elif line.startswith("Lines per out = "):
                linesOut= int(line.replace('Lines per out = ',''))
            elif line.startswith("Score per out = "):
                scoreOut = int(line.replace('Score per out = ',''))
            elif line.startswith("Reward comments = "):
                countOff = "true" in (line.replace('Reward comments = ','').replace('\n','')).lower()
            elif line.startswith("Score to win = "):
                scoreToWin = int(line.replace('Score to win = ','').replace('\n',''))
            elif line.startswith("Mutate best = "):
                muteBest = int(line.replace('Mutate best = ','').replace('\n',''))
            elif line.startswith("Point mutations = "):
                pointMute = float(line.replace('Point mutations = ','').replace('\n',''))  
            elif line.startswith("Mate error = "):
                mateError = float(line.replace('Mate error = ','').replace('\n',''))
            elif line.startswith("Rescore = "):
                rescore = bool(line.replace('Rescore = ','').replace('\n',''))
            elif line.startswith("Max running = "):
                maxRunning = int(line.replace('Max running = ','').replace('\n',''))
            elif line.startswith("Words1 = "):
                word1.append(line.replace('Words1 = ','').replace('\n',''))
            elif line.startswith("Words2 = "):
                word2.append(line.replace('Words2 = ','').replace('\n',''))
            elif line.startswith("Words3 = "):
                word3.append(line.replace('Words3 = ','').replace('\n',''))
            elif line.startswith("Words4 = "):
                word4.append(line.replace('Words4 = ','').replace('\n',''))
            elif line.startswith("Words5 = "):
                word5.append(line.replace('Words5 = ','').replace('\n',''))
            elif line.startswith("Code = "):
                code.append(line.replace('Code = ','').replace('\n',''))
                gotCode = True
            elif line.startswith("Header start"):
                while True:
                    pos += 1
                    line = script[pos]
                    if len(line) > 0 and not line.startswith("Header end"):
                        header.append(line.replace('\n',''))
                        gotHeader = True
                    else:
                        break
            elif line.startswith("Footer start"):
                while True:
                    pos += 1
                    line = script[pos]
                    if len(line) > 0 and not line.startswith("Footer end"):
                        footer.append(line.replace('\n',''))
                        gotFooter = True
                    else:
                        break
        pos += 1
    
    diversity = errorMult = 1        
    fileScore = [0]*seeds
    done = False

    headLen = len(header) + 4
    footLen = len(footer) + 2        
                        
    print "Code:", code
    print "Words1:", word1
    print "Words2:", word2
    print "Words3:", word3
    print "Words4:", word4
    print "Words5:", word5
    print "Header", header
    print "Footer", footer
        
    randList = []
    for pos in range(seeds):
        randList.append(pos)
   
    if not carryOn or not os.path.exists(name):
        if not os.path.exists(name):
            os.makedirs(name)    
        generation = 0
        for pos in range(seeds):
            newCode = makeLines(word1,word2,word3,word4,word5,code,lines) 
            makeFile(header, newCode, footer, name, lines, linesOut, scoreOut, pos,False, generation)
            logFile = open(logName(name,pos),'w')
            logFile.write('New seed generated at startup\n')
            logFile.close()
        mainLog = open(name + '/GenLog.txt','w')
        mainLog.write("Starting at generation 0, " + str(time.asctime( time.localtime(time.time()) )) + '\n')
        mainLog.close()
    else:
        getGen = open(name + '/GenLog.txt')
        temp = getGen.readlines()
        generation = int(temp[-1].split(' ')[1])+1
	getGen.close()

            
    while not done:
                
        print "Generation:", generation
        
        canRun = seeds
        ran = 0
        time.sleep(0.1)
        for pos in range(seeds):
            if pos not in toKeep or rescore:
                scoreFile = open(scoreName(name,pos),'w')
                scoreFile.write(str(noLoadScore))
                scoreFile.close()
                if maxRunning != False:
                    while getNumProc(name) >= maxRunning:
                        time.sleep(5)
                try:
                    print "Running seed:", fileName(name,pos), "Generation:", generation
                    subprocess.Popen([sys.executable,fileName(name,pos)])
                    ran += 1
                    if ran == 5:
                        time.sleep(0.03)
                        ran = 0
                except:
                    print "Could not run seed", fileName(name,pos)
                    
        print "Waiting until processes complete"
        while getNumProc(name) >= 0:
                        None

        for pos in range(seeds):
            if pos not in toKeep or rescore:
                scoreFile = open(scoreName(name,pos))
                line = scoreFile.read()
                scoreFile.close()
                multiplicator = 1
                if '-' in line:
                    line = line.replace('-','')
                    multiplicator = -1   
                try:
                    tempScore =  multiplicator*float(line)
                except:
                    tempScore = noLoadScore
                if tempScore == noLoadScore:
                    canRun -= 1
                
                if tempScore != noLoadScore and countOff:
                    tempScore += countHidden(fileName(name,pos))/(lines/5)
    
                fileScore[pos] = tempScore
                logFile = open(logName(name,pos),'a+b')
                logFile.write('Generation: %s Score: %s\n' % (str(generation), str(tempScore)))
                logFile.close()
                
        diversity = float(len(set(fileScore)))/seeds 
        errorMult = adjustError(diversity)
        
        """if punishCopies != 0:
            for pos in range(seeds-1):
                fileScore[pos] -= fileScore[pos+1:].count(fileScore[pos])*punishCopies"""

        meanScore = sum(fileScore)/seeds
        rankScore = sorted(fileScore)[:]

        rankInts = []
        for pos in range(seeds):
            rankInts.append('%.2f' % rankScore[pos])

        medianScore =  rankScore[len(rankScore)/2]
        replaceCutOff = rankScore[new-1]
        killCutOff = rankScore[new+kill-1]
        muteCutOff = rankScore[new+kill+muteBest-1]
        
        toKeep = []
        toKill = []
        toMute = []
        toReplace = []
                
        if replaceWeak:
            gottaGo = kill+new+muteBest
            extra = 0.9*(seeds-gottaGo)
            extraReplace = extra*(new/gottaGo)
            extraKills = extra*(kill/gottaGo)
            extraMutes = extra*(muteBest/gottaGo)
                          
        ID = randList.index(fileScore.index(min(fileScore)))
        random.shuffle(randList)
        for pos in range(seeds):
            value = fileScore[randList[pos]]
            randPos = randList[pos]
            if fileScore[randPos] > fileScore[randList[ID]] and fileScore[randPos] != noLoadScore:
                ID = pos
            if (value <= replaceCutOff or (value == noLoadScore and replaceWeak)) and len(toReplace) < new+extraReplace:
                toReplace.append(randPos)
            elif (value <= killCutOff or (value == noLoadScore and replaceWeak)) and len(toKill) < kill+extraKills:
                toKill.append(randPos)
            elif (value <= muteCutOff or (value == noLoadScore and replaceWeak)) and len(toMute) < muteBest+extraMutes:
                toMute.append(randPos)
            else:
                toKeep.append(randPos) 

        
        bestScore =  fileScore[randList[ID]]
        
        print "Maximum score: %s Mean: %s Median: %s" % (bestScore,meanScore,medianScore)
        print "Replace cutoff: %s Kill Cutoff: %s" % (replaceCutOff,killCutOff)
        
        mainLog = open(name + '/GenLog.txt','a+b')
        mainLog.write("Gen: %s Best: %s Seed: %s Running: %s Time: %s\n" % (str(generation), '%.2f' % bestScore, ID, str(canRun), time.asctime( time.localtime(time.time()) )))
        mainLog.close()
        
        delay = 0.01
        delayEvery = 5
        delayCount = 0
        
        for killOne in toKill:
           print "Replacing ID with random breed: ", killOne
           index1 = fileName(name,str(random.choice(toKeep)))
           index2 = fileName(name,str(random.choice(toKeep)))
           while index1 == index2:
               index2 = fileName(name,str(random.choice(toKeep)))          
           newCode = breedScripts(index1,index2,headLen,footLen,mateError*errorMult,word1,word2,word3,word4,word5,code)
           scoreFile = open(scoreName(name,killOne),'w')
           scoreFile.write(str(noLoadScore))
           scoreFile.close()
           makeFile(header, newCode, footer, name, lines, linesOut, scoreOut, killOne,True, generation)
           logFile = open(logName(name,killOne),'w')
           logFile.write('New script bred on generation %s from scripts %s and %s\n' % (str(generation),index1,index2))
           logFile.close()
           delayCount += 1
           if delayCount % delayEvery == 0:
               time.sleep(delay)
           
        for muteOne in toMute:
           print "Replacing ID with strong mutant: ", muteOne
           newCode = mutateBest(fileName(name,ID),headLen,footLen,pointMute*errorMult,word1,word2,word3,word4,word5,code)
           scoreFile = open(scoreName(name,muteOne),'w')
           scoreFile.write(str(noLoadScore))
           scoreFile.close()
           makeFile(header, newCode, footer, name, lines, linesOut, scoreOut, muteOne, True, generation)
           logFile = open(logName(name,muteOne),'w')
           logFile.write('New script mutated on generation %s from scripts %s\n' % (str(generation),ID))
           logFile.close()
           delayCount += 1
           if delayCount % delayEvery == 0:
               time.sleep(delay)
        
        for replaceOne in toReplace:
            print "Replacing ID with novel seed: ", replaceOne
            newCode = makeLines(word1,word2,word3,word4,word5,code,lines)
            makeFile(header, newCode, footer, name, lines, linesOut, scoreOut, replaceOne, False, generation)
            scoreFile = open(scoreName(name,replaceOne),'w')
            scoreFile.write(str(noLoadScore))
            scoreFile.close()
            logFile = open(logName(name,replaceOne),'w')
            logFile.write('New script spawned on generation %s' % str(generation))
            logFile.close()
            delayCount += 1
            if delayCount % delayEvery == 0:
               time.sleep(delay)
            
        if bestScore == scoreToWin:
            print "Optimal result recieved at generation %s, please check script %s to verify!" % (str(generation),fileName(name,ID))
            mainLog = open(name + '/GenLog.txt','a+b')
            mainLog.write("Optimal result recieved at generation %s, please check script %s to verify!" % (str(generation),fileName(name,ID)))
            mainLog.close()
            quit()
        
        generation +=1
        
        if generation > 0 and generation%increment == 0:
            print rankInts
            print "Interval Reached, please enter 'quit' in next", inputDelay, "seconds to quit"
            print "Kept: %s Bred: %s Novel: %s Mutated: %s" % (len(toKeep),len(toKill),len(toReplace),len(toMute))
            print "Maximum score: %s Mean: %s Median: %s" % (bestScore,meanScore,medianScore)   
            print "Diversity: %s%% Error Adjustment: %s" % (100*diversity,errorMult)
            i, o, e = select.select([sys.stdin], [], [], inputDelay)
            if (i):
                if sys.stdin.readline().strip().lower() == 'quit':
                    print "Quit command recieved, exiting now"
                    quit()
                else:
                    print "No input recieved, continuing process"
                             
main()
quit()
