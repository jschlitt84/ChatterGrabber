import cPickle
import KwikECache as kwik
import sys, os

#cache, field, word, outfile

data = dict()
print sys.argv[1:]
pickleIn = open(sys.argv[1], "rb")
pickleLoaded = cPickle.load(pickleIn)
pickleOut = {key:item for key, item in pickleLoaded.iteritems() if sys.argv[3].lower() in item[sys.argv[2]].lower()}
print "Pickle %s reduced from size %s to %s" % (sys.argv[1],len(pickleLoaded.keys()),len(pickleOut.keys()))
kwik.updateCache(pickleOut,sys.argv[4],25)