import cPickle
import KwikECache as kwik
import sys, os

data = dict()
pickleIn1 = open(sys.argv[1], "rb")
pickleLoaded1 = cPickle.load(pickleIn1)
pickleIn2 = open(sys.argv[2], "rb")
pickleLoaded2 = cPickle.load(pickleIn2)
pickleLoaded1.update(pickleLoaded2)
kwik.updateCache(pickleLoaded1,sys.argv[3],25):