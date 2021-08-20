from __future__ import print_function
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    with open('etc/hosts','r',encoding='utf-8') as f:
        data = f.read()
    print(data)
    with open('C:/Windows/System32/drivers/etc/hosts','w',encoding='utf-8') as j:
        new = j.write(data)

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)