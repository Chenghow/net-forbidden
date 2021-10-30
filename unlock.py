from __future__ import print_function
import ctypes, sys
##获取管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    with open('etc/origin','r',encoding='utf-8') as f:
        data = f.read()##读取备份的hosts
    print(data)
    with open('C:/Windows/System32/drivers/etc/hosts','w',encoding='utf-8') as j:
        new = j.write(data)##写入系统hosts

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)