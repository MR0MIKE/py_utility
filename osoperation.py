#!python
import os
print '===============OS info:'
print os.name
print os.environ
print os.environ.get('PATH')

print '===============OS join and spilt:'
print 'current folder: '+ os.path.abspath('.')
newpath = os.path.join(os.path.abspath('.'),'testdir')
print 'newpath: '+newpath
os.rmdir(newpath)
os.mkdir(newpath)

strfile = "C:\\dir\\thest.txt"
print 'path split: ' + strfile
spPath =  os.path.split(strfile)
print spPath[0]+' + '+spPath[1]
print "splitext: "
sptext = os.path.splitext("C:\\dir\\thest.txt")
print sptext

dirnow = "G:\\"
print '==== list files in dir: '+dirnow
print os.listdir(dirnow)

print '==== list folder in current dir: '
for x in os.listdir('.'):
    if os.path.isdir(x):
        print x
        
print '==== list file in current dir: '        
for x in os.listdir('.'):
    if os.path.isfile(x):
        print x
        
print '==== list .py file: '        
for x in os.listdir('.'):
    if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
        print x


