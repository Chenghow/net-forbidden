from __future__ import print_function
import ctypes, sys
##获取管理员权限
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    with open('C:/Windows/System32/drivers/etc/hosts','r',encoding='utf-8') as a:
        origin = a.read()##读取系统hosts
    with open('etc/hosts','r',encoding='utf-8') as f:
        data = f.read()##打开自带hosts文件
    with open('etc/origin','w',encoding='utf-8') as b:
        backup = b.write(origin)##备份
    with open('C:/Windows/System32/drivers/etc/hosts','w',encoding='utf-8') as j:
        new = j.write(data)##写入系统hosts

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
