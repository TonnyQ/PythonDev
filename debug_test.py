# -*- encoding:utf-8 -*-
#错误处理
try:
    print('try...')
    r = 10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End')

#show:对可能出现错误的代码try，如果真的发生错误，错误发生后的代码将不再执行
#将进入except处理错误，最后如果存在finally，则进入finally。如果没有发生错误
#将不会执行except语句，还可以针对不同错误类型进入不同的except语句块处理。此外
#还可以在except后面加一个else，当没有发生错误时，会自动执行else语句。
try:
    a = 3 / 2
except ValueError as e:
    print('valueerror:',e)
else:
    print('no happen error')

#python的错误其实也是class，所有的错误类型都继承自BaseException,所以使用except时需要注意的是
#它不但能捕获该类型错误，也能处理其子类。
try:
    a = int('a')
except ValueError as e:
    print('value error')
except UnicodeError as e:
    print('UnicodeError') #no execute,because UnicodeError is ValueError subclass

#调用堆栈
#如果错误没有被捕获，就会一直往上抛，最后被python的解释器捕获，打印一个错误信息，然后程序退出
#调试错误时，查看错误堆栈，应该从上往下看，错误的最终原因就在堆栈的最底层

#记录错误
#如果不捕获错误，自然可以让python解释器打印错误堆栈，但程序也被结束了。我们可以自己捕获错误，
#并打印错误堆栈信息，然后分析错误原因，同时，让程序继续执行。
import logging #python内置的log模块
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('end======')

#抛出错误
#因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建
#并抛出的。python内置函数会抛出很多类型的错误，我们也能自定义抛出错误
class FooError(ValueError):
    pass
def foos(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value : %s' % s)
    return 10 / n
#只有必要时才需要定义自己的错误类，否则尽量使用系统提供的错误类型
try:
    foos('0')
except FooError as e:
    print('FooError :',e)

#捕获错误，然后继续向上层抛出错误，raise语句如果不带参数，则会把当前错误原样抛出
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError:',e)
        raise #继续向上抛出错误

#断言assert,需要小心的使用assert，因为它会让程序错误，停止执行。可以在python解释器时使用-o参数关闭assert
def hoo(s):
    n = int(s)
    #assert n != 0,'n is zero' #assert将判断表达式是否为true，如果不为true，则根据运行逻辑抛出AssertionError
    return 10 / n
def mains():
    foo('0')
#mains()

#logging模块,logging不会抛出错误，终止程序，而且可以统一的关闭，允许指定记录信息的级别
logging.basicConfig(Level=logging.error)
logging.exception('test loggin')

#pdb,启动python的调试器pdb，让程序以单步方式执行，可以随时查看运行时状态
#python3 -m pdb err.py
#输入命令：l，来查看代码
#输入命令：n，可以单步执行代码
#输入命令：p ‘变量名’，来查看变量的value
#输入命令：q，结束调试

#pdb.set_trace(),使用p命令查看变量，或者命令c继续执行
import pdb
s = '0'
n = int(s)
pdb.set_trace() #运行到这里自动的暂停
print(1/n)
