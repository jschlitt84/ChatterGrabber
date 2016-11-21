import os
import datetime

def setLastRan():
    pid = os.getpid()
    procName = "TwitterSpout_%s" % pid
    strTime = str(datetime.datetime.now())
    print procName,strTime
    os.environ[procName]=strTime

setLastRan()
spoutEnv = [key for key in os.environ.keys() if key.startswith('TwitterSpout_')]
print spoutEnv