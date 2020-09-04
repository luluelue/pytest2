# coding:utf-8
from inspect import isfunction
import types
import sys

# 在虚拟环境下
# easy_install pydevd-pycharm.egg

# 修改系统变量：PYTHONDONTWRITEBYTECODE=x
# 删除pyc并，禁止pyc的生成

def debug():
    # 直接导入egg文件也能够执行
    sys.path.append("C:/Users/11329/Desktop/pydevd-pycharm.egg")
    # sys.path.append("C:/Users/11329/Desktop/pydevd-pycharm")
    import pydevd
    pydevd.settrace('localhost', port=11111, stdoutToServer=True, stderrToServer=True)
    # 打印python解释器的位置
    print sys.executable
    print sys.path
    print "aaaaa"
    print "aaaaa"
    print "aaaaa"



if __name__ == '__main__':
    debug()
