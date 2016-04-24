#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass

s = Student()
s.name = 'tonny' #bind name attribute
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) #bind a set_age method
s.set_age(34)
print(s.age)

s2 = Student()
#s2.set_age(20) 为实例绑定的方法，对于另一个实例无效

#为了给所有实例绑定方法，需要给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score #动态绑定函数给Student类
s2.set_score(333)
print(s2.score)

s.set_score(10000)
print(s.score)

#使用__slots__,如何限制实例的属性？比如只允许对student实例添加name和age属性
#为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__solts__变量，来限制该class实例能添加的属性
class Techer:
    __solts__ = ('name') #__solts__不起作用？？

t = Techer()
t.name = 'tonny'
t.age = 10
t.score = 100
print(t.name,t.age,t.score)

#python内置@property装饰器就是负责把一个方法变成属性调用，如果只设置setter而不设置getter则为只读属性
class Student2(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self.__score = value

s = Student2()
s.score = 60 #此时不是为s绑定属性score，而是调用score方法
print(s.score)

#多重继承,通过多重继承，一个子类就可以同时获得多个父类的所有功能
#MixIn,在设计类的继承关系时，通常主线都是单一继承，但是如果需要‘mix’额外的功能时，通过多重继承实现，这叫做’mixin
#mixin的目的是给一个类增加多个功能，这样在设计类时，我们优先考虑通过多重继承来组合多个Mixin功能，而不是设计多
#层次的复杂的继承关系
#多重继承的优先级：如果一个类多重继承A,B，并且AB有同名的方法，那么A,B的继承顺序就很重要了，
#多重继承是在存在共同方法的时候，是继承首个父类的方法
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('running...')

class Flyable(object):
    def fly(self):
        print('flying...')

class Dog(Mammal,Runnable): #多重继承
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Runnable):
    pass

class Ostrich(Bird,Flyable):
    pass

#定制类
#1. __str__属性
class Car(object):
    def __init__(self,name):
        self.__name = name

    def __str__(self): #相当于自定义的tostring
        return 'Car object (name : %s)' % self.__name

c = Car('qq')
print(c)

#2. __iter__ ,如果想返回一个迭代对象，然后python的for循环就会不断的调用该迭代对象的__next__方法循环取下一个值
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

#3. __getitem__,__iter__返回的只是一个Iterator对象，并不是已经完全生成了一个list
class Fib2(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            return _genlist(n)
        if isinstance(n,slice):
            return _genslice(n)

    def _genlist(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a + b
        return a

    def _genslice(self,n):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a,b = 1,1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a,b = b,a + b
        return L

f = Fib2()
#print(f[5])
#print(f[0:4])

#使用枚举类,当定义常量时，通常使用大写变量通过整数来定义，更好的方法是使用python提供的Enum类来实现
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value) #value属性是自动赋值给成员的int常量，默认从1开始

from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复的值
day1 = Weekday.Mon
print(day1)
print(Weekday['Tue'])
print(Weekday.Tue.value)
