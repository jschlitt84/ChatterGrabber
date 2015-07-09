import cPickle
import sys

pickleIn = open(sys.argv[1], "rb")
pickleLoaded = cPickle.load(pickleIn)
pickleIn.close()

keys = pickleLoaded.keys()
newPickle = dict()

for key in keys:
    hasCoords = ']' in key
    newKey = key.split(']')[0] + ']'*hasCoords
    print key,'\t-->\t',newKey
    newPickle[newKey] = pickleLoaded[key]
    
pickleOut = open(sys.argv[2],"wb")
cPickle.dump(newPickle, pickleOut)
pickleOut.close()
print 'Pickle shortened from',len(pickleLoaded.keys()),'to',len(newPickle.keys())
print 'Operation complete'
quit()