#!/usr/bin/python2.7

import urllib2
from time import sleep

'''
Impliment for clan names.
Add sleep(.5)
Make into a class.
functions. etc

'''
url = 'http://gunz.ijji.com/shop/checkCharName.nhn?characterName='
names = []

print "Starting..."
with open('word_list.txt', 'r') as f:
    words = f.read().split()

for word in words:    
    req = urllib2.urlopen(url + word) 
    if 'true' not in req.read().lower():
        continue
    names.append(word)
	sleep(.5)
with open('name_list', 'w') as f2:
    f2.write(str(names))

print "Finished!"
