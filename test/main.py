from inspect import signature
from inspect import isfunction
import types
import sys


class Test():

    def __init__(self, name):
        self.name = name

    def main1(self):
        print("我是类函数")

    def main2(self, arg1, aa=100):
        print("函数2")


def main():
    test = Test("张三")
    # print(dir(test))
    # print(test.__dict__.keys())
    for key in dir(test):
        print(key)
        func = getattr(test, key)
        if (callable(func)):
            print(signature(func))
        # if isfunction(func):



if __name__ == '__main__':
    main()
