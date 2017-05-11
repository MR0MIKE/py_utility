#! python

import os

suffix = '.txt'  # find the file u want

x = os.path.abspath('.')

dirthings = os.listdir('.')

print x

print 'open the folder:'
with open("imageFile.txt","w") as fp:
    for i in dirthings:
        print os.path.splitext(i)[1]
        if os.path.isfile(i) and os.path.splitext(i)[1] == suffix:
            print "get it:"
            print i
            fp.write(i+'\n');
            
            