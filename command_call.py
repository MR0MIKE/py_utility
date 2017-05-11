#! python
# os.system
# ShellExecute
# CreateProcess
# ctypes call kernel32.dll

#CreateProcess(appName, commandLine , processAttributes , threadAttributes , bInheritHandles ,dwCreationFlags , newEnvironment , currentDirectory , startupinfo )
#ShellExecute(hwnd, op , file , params , dir , bShow )

import os
import subprocess

# import win32api
# import  win32process

os.mkdir("goodfeeling")
exename = 'H:\JavaWorkSpace\pyPractice\getArgc.exe'
exename = 'H:\JavaWorkSpace\pyPractice\getArgc_no_enter.exe'
arg1 = ' test'
arg2 = ' 12'
arg3 = ' 14' 

print '================= test subprocess: '
p=subprocess.Popen(exename, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
result = p.communicate(input=arg1+arg2+arg3)
res = result[0].decode()
print res



print '================= test os.system: '
os.system(exename+arg1+arg2+arg3)
