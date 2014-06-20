import sys
sys.path.insert(0, 'libraries')
import subprocess
from time import sleep



format = "\033[91m\033[1m"
end = "\033[0m"
secondsPerDay = 86400
daysToRefresh = 5
delay = 600
count = 0
sleepEvery = (secondsPerDay*daysToRefresh)/delay

while True:
    count += 1
    try:
        fileIn = open('daemonScripts/'+str(sys.argv[1]))
        print "Opened file",sys.argv[1]
    except:
        try:
            fileIn = open(str(sys.argv[1]))
            print "Opened file",sys.argv[1]
        except: 
            fileIn = open('daemonScripts/'+'gdiAccounts')
            print "Opened file gdiAccounts"
    
    urls = set()
    
    content = fileIn.readlines()
    fileIn.close()
    
    print format+"\n\n(Re)Loading URL list",end
    
    for line in content:
        if '.url=' in line.replace(' ','') and not line.startswith('#'):
            urls.add(line[line.index('https://'):-1])
        
    for url in urls:
        print format + "GDI URL:", url,end
    running = set()
    
    ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
    processes = ps.split('\n')
    
    print "\n"
    for process in processes:
        if 'python' in process:
            for url in urls:
                if url in process:
                    foundUrl = process[process.index('https://'):]
                    print format+"RUNNING:",foundUrl,end
                    running.add(foundUrl)
                    
    if count%sleepEvery == 0:
        None
    
    notRunning = set.difference(urls,running)
    for item in notRunning:
        print format+"NOT RUNNING:",item.replace('\n',''),end
    print "\n"
    for url in notRunning:
        try:
            subprocess.Popen(['python','TwitterSpout.py', url])
            sleep(30)
        except:
            print "Process",url,"has stopped"
            None
    sleep(delay)
