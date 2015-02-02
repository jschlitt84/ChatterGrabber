from time import sleep
from shutil import copyfile
while True:
   copyfile('caches/GeoPickle2.txt','caches/GeoPickle.txt')
   sleep(300)
