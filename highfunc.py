#!/usr/bin/env python3
#切片，取一个list或者tuple的部分元素是常见的操作
l = ["addd",'dses',22,3,2,2]
#取前n个元素
a = l[0:3] #取0，1，2单个元素，不包含尾索引
print(a)

#切片操作支持从尾部开始，最后一个元素的索引为-1,必须指定步长为负数
b = l[-1:-3:-1]
print(b)

#tuple同样支持切片
c0 = (1,33,3,4)
c = c0 [:3] #create a new tuple
print(id(c0),id(c),type(c),c)

#字符窜同样可以看做是一个list，每个字符为一个元素，所以字符窜同样能够切片操作
d = 'abdende'[:4]
print(d)

#迭代操作,如果给定一个list或者tuple，可以通过for循环来遍历这个list或tuple，这种遍历称之为迭代
#在python中for循环抽象程度高于其他语言，python的for不仅可以用在list上，还可以作用域可迭代对象
dic = {'a':11,'b':3232,'c':455}
for key in dic: #默认情况下，dict迭代的是key，如果要迭代value使用for value in dic.values()
    print(key,dic[key])

for k,v in dic.items():
    print(k,v)

for value in dic.values():
    print(value)

#string是可迭代对象
for ch in 'ddesesse':
    print(ch)

#怎么判断一个对象是否可迭代？通过collections模块的iterable类型判断
from collections import Iterable
print(isinstance("abc",Iterable))
print(isinstance(123,Iterable))
print(isinstance([1,2,3],Iterable))

#如果实现下标迭代？python内置了enumerate函数可以把一个list变成索引-元素对。
for i,value in enumerate([1,2,3,2]):
    print(i,value)

for (x,y) in [(1,2),(3,'d'),('3','33')]:
    print(x,y)

ss = [x * x for x in range(1,11)]
print(ss)

ss = [x * x for x in range(1,11) if x % 2 == 0]
print(ss)

ss = [m + n for m in 'abc' for n in 'xyz']
print(ss)

import os #导入os模块
ss = [d for d in os.listdir('.')]
print(ss)

d = {'x':'a','y':'b','z':'c'}
ss = [k + v for k,v in d.items()]
print(ss)

#在python中能够通过在循环过程中计算后续元素的机制称为生成器(generator)

#l与g的区别仅仅在于一个使用[],一个使用(),l是list，而g是genrator,genrator保存的算法，而list保存的是元素
#使用generator的最大好处是节约内存空间，因为它仅仅保存算法，这对于大量可推测数据很高效
l = [x * x for x in range(1,10)]
print(type(l))
print(l)
g = (x * x for x in range(1,10))
print(type(g))
for n in g:
    print(n)

#定义一个斐波拉切的generator，如果一个函数中包含yield关键字，那这个函数就是一个生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(type(fib))
f = fib(6)
print(f)

#理解函数与生成器的区别：函数是顺序执行的遇到return语句或者最后一行的函数语句就返回，而generator的函数
#在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
print(next(f))
for n in f:
    print(n)

#迭代器
#for循环可用于三类数据类型：
#1.集合数据类型，list、tuple、dict、set、str
#2.generator，包括生成器和带yield的generator函数
#3.可迭代对象Iterable，使用isinstance()判断一个对象是否是Iterable
from collections import Iterable
isinstance([],Iterable)
isinstance({},Iterable)
isinstance([x for x in range(10)],Iterable)
isinstance(100,Iterable)

#Iterator对象，能够调用next函数并不断返回下一个值得对象
#生成器对象都是Iterator对象，而list，dict，str虽然是可迭代对象但是不是Iterator
#Iterator对象表示的是一个数据流，Iterator对象可以被next函数调用并不断返回下一个数据，
#直到没有数据时抛出StopIteration错误。可以吧这个数据流看做一个有序序列，但是我们却不提前知道序列长度
#Iterator甚至可以表示一个无限大的数据流，而使用list是永远不可能存储全体自然数的。
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance({},Iterator))
print(isinstance('dddd',Iterator))
