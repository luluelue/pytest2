# coding:utf-8
from inspect import isfunction
import types
import sys

# 在虚拟环境下
# easy_install pydevd-pycharm.egg
# 安装完成后 sys.path = ['G:\\py_project\\pytest1\\test', 'C:\\Windows\\SYSTEM32\\python27.zip', 'G:\\py_project\\pytest1\\venv27\\DLLs', 'G:\\py_project\\pytest
# 1\\venv27\\lib', 'G:\\py_project\\pytest1\\venv27\\lib\\plat-win', 'G:\\py_project\\pytest1\\venv27\\lib\\lib-tk', 'G:\\py_project\\pytes
# t1\\venv27\\Scripts', 'C:\\Python27\\Lib', 'C:\\Python27\\DLLs', 'C:\\Python27\\Lib\\lib-tk', 'G:\\py_project\\pytest1\\venv27', 'G:\\py_
# project\\pytest1\\venv27\\lib\\site-packages', 'G:\\py_project\\pytest1\\venv27\\lib\\site-packages\\pydevd-pycharm.egg']
def debug():
    sys.path.append("C:/Users/11329/Desktop/pydevd-pycharm")
    import pydevd
    pydevd.settrace('localhost', port=11111, stdoutToServer=True, stderrToServer=True)
    print sys.executable
    print sys.path
    print "aaaaa"
    print "aaaaa"
    print "aaaaa"
    pass


if __name__ == '__main__':
    debug()
