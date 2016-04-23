#!/usr/bin/env python3

#函数是python内建支持的一种封装。函数式编程允许把函数作为参数传入另一个函数，还允许返回函数。
x = abs #函数本身也可以赋给变量
print(type(x))
print(x(-10))

#函数名也是变量，函数名其实就是指向函数的变量
#abs = 10
#abs(-10)

#传入函数，函数参数也能接受变量，可以把函数作为参数传入函数
def add(x,y,f):
    return f(x) + f(y)

sum = add(-5,6,abs); #equal abs(-5) + abs(6) = 11
print(sum)

#map & reduce
#map:接受两个参数，一个是函数，一个是Iterable,map将传入的函数依次作用于序列中的每一个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x;

r = map(f,[1,2,3,4]) #r is Iterator object,type is map
print(type(r))
for n in r:
    print(n)

#reduce:把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce #reduce is high func tools,must import reduce
def add(x,y):
    return x + y;
sum = reduce(add,[1,3,5,7,9])
print(sum)

#filter用于过滤序列,接受一个函数和一个序列，把传入函数依次作用于每个元素，然后根据返回值是true或false决定保留还是丢弃元素
def is_odd(n):
    return n % 2 == 1
r = list(filter(is_odd,[1,2,3,4,5,6,7])) #filter返回一个iterator对象
print(r)

#sorted：python内置的对序列排序的方法
ret = sorted([3,2,5,4,7])
print(ret)

#sorted还能接受一个key函数来实现自定义的排序,key指定的函数将作用于每个元素，并根据key函数返回的结果进行排序
#对比原始的list和经过key处理过的list，然后sorted函数按照keys进行排序，并按照对应关系返回list相应的元素
ret = sorted([-988,2,4,3,222],key=abs)
print(ret)

#返回函数，函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum(): #定义内部函数sum可以引用外部函数的参数和局部变量
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum #返回函数时，相关参数和变量都保存在返回函数中，这称为闭包
f = lazy_sum(1,2,3,4,32,3222)
print(f)
print(f())
f2 = lazy_sum(1,2,3,4,32,3222)
print(f == f2) #f is not f2

#函数闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
#闭包使用原则：返回函数不要引用任何循环变量，或者后续会发生变化的变量
#因为返回的函数引用了变量i，但它并非立刻释放。等三个函数都返回时，所引用的变量i都已经变为3
f1,f2,f3 = count()
print(f1()) #9
print(f2()) #9
print(f3()) #9

def count_ex():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count_ex();
print(f1()) #1
print(f2()) #4
print(f3()) #9

#匿名函数，当我们传入函数时，有时不需要显示地定义函数，直接传入匿名函数更方便
ret = list(map(lambda x: x * x,[1,2,3,4,3])) #此时lambda x: x * x为匿名函数
print(ret) #1,4,9,16,9

#lambda关键字表示匿名函数，冒号前则为匿名函数的参数，后面的为函数体
#匿名函数的限制为只能有一个表达式，不用谢return，发挥至就是该表达式的结果
f = lambda x: x * x
ret = list(map(f,[2,3,4,5]))
print(ret)

#装饰器，由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2016-4-23')

f = now
print(f())

#函数对象有一个__name__属性，通过它可以取得函数的名称
print(f.__name__)

#利用decorator增强函数的动态功能
def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log2('ddddd') #decorator,equal now2 = log(now2) now2 = log2('ddddd')(now2)
def now2():
    print('2016-4-23')

print(now2())

#偏函数，python的functools模块提供了很多有用的功能，其中一个便是偏函数(不同于数学上的偏函数)
print(int('12333'))
print(int('12333',base=8))
print(int('12333',base=16))
print(int('111111',base=2))

import functools
int2 = functools.partial(int,base=2) #把一个函数的某些参数给固定住，返回一个新函数
print(int2('10000000'))
