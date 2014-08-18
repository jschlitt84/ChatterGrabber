import cPickle
import KwikECache as kwik
import sys, os

#cache, field, word, outfile

data = dict()
print sys.argv[1:]
pickleIn1 = open(sys.argv[1], "rb")
pickleLoaded1 = cPickle.load(pickleIn1)
pickleOut = {key:item for key, item in pickleLoaded1.iteritems() if sys.argv[3].lower() in item[sys.argv[2]].lower()}
print pickleOut.keys()
kwik.updateCache(pickleOut,sys.argv[4],25)