#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module' #module doc,任何模块的第一个字符串都被视为模块的文档注释
__author__ = 'tonny'

import sys #import other module

def test():
    args = sys.argv #sys有一个argv变量，用list存储了命令行的所有参数，argv至少存储一个元素，第一个参数就是模块的名字
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')


#如果在其他模块中导入该模块，该条件判断将为false，只有直接运行该模块时才为true。一般在此处进行单元测试
if __name__ == '__main__': #在命令行运行hello模块时，解释器把一个特殊的变量__name__置为__main__
        test()
