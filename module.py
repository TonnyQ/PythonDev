#!/usr/bin/env python3
#在python中一个.py文件就是一个模块。使用模块能够提高代码的可维护性，便于代码的重用，还能够避免
#命名冲突，需要注意不要与保留字以及内置函数命名冲突。为了避免模块名冲突，python引入了packeage。
#package是按文件目录组织模块的，文件目录中必须存在一个__init__.py文件，这个文件的模块名为package

#如何使用模块?
#在一个模块中，可以定义很多的函数和变量，但有的函数和变量我们希望是public，部分函数和变量是private
#在python中是通过_前缀来实现的，正常的函数和变量都是public可以被直接引用，类似于__xxx__这样的变量
#是特殊变量，可以直接被引用，但是有特殊用途，一般我们的变量名不要使用这种方式定义。类似于_x或者__xxx
#这样的变量和函数是private的‘不应该’被外部直接引用。python并没有一种方法约束外部模块访问private函数和变量

#在python中安装第三方模块是通过pip包管理工具完成的。
#python3对应的pip3，python2则对应于pip，一般第三方库都会在pypi.python.org网站注册
#安装模块命令：pip install '模块名'

#模块搜索路径
#当我们试图加载一个模块时，python会在指定的路径下搜索对应的py文件，如果找不到则报错
#默认情况下，python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径
#存放在sys模块的path变量中
import sys
print(sys.path)

#如果需要添加自定义的搜索目录有两种办法：
#1. sys.path.append('path'),运行时生效，运行结束后失效
#2. 在python的环境变量PYTHONPATH中，该环境变量的内容会被自动添加到模块搜索路径中

#使用自定义的模块
import Hello
Hello.test()
