#!/usr/bin/env python3

#在python中所有的数据类型都可以视为对象，当然也可以自定义对象。自定义对象的数据类型就是面向对象中的类。
#面向对象的抽象程度比函数要高，其设计思想是抽象出Class，根据Class创建类的Instance。
#总之，一切皆对象。

#和静态类型语言不同，python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然是同一类的实例，
#但拥有的变量名称都有可能不同,甚至属性的数量都不同，因为python允许动态绑定

class Student(object): #(object)表明类Student继承自object类
    def __init__(self,name,score): #__init__方法的第一个参数永远是self,表示创建实例本身
        self.name = name
        self.score = score #面向对象编程的一个重要特点就是数据封装

    def print_score(self): #和普通函数不同，在类中定义方法，方法的第一个参数为self，调用时不用传入该参数
        print('%s : %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'a'
        elif self.score >= 60:
            return 'b'
        else:
            return 'c'

bart = Student('tonny',80)
bart.print_score()
bart.age = 10
print(bart.age)

dev = Student('test',30)
#print(dev.age) error:dev has not attribute 'age'
print(dev.score) #外部仍可以直接访问class的属性

#如果想要让内部属性不被外部访问可以把属性的名称前加上两个'__',在python中，实例变量的名如果以__开头，
#就变成了私有private，只有内部可以访问，外部不能访问
class StudentEx(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

test = StudentEx('test',90)
#print(test.__name)  #__name attribute is private,cann't access
test.print_score()
print(test.get_name())
test.set_name('dddd')
print(test.get_name())

#变量访问限制：（python本身没有任何机制限制变量的访问域，但要写出良好的代码，需要注意养成好的命名习惯）
#1.__xxx__为特殊变量，从外部模块可以直接访问，相当于public，但这些变量有特殊用途，一般变量不建议这样命名
#2._xxx的实例变量或者模块变量，”不应该”可以被外部访问，但是可以从外部直接访问，一般这样的变量表明建议为private
#3.__xxx的实例变量一般不能被外部直接访问，这是因为python解释器将其变为_Class__xxx,可以通过访问后者访问

#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

#继承能够获得父类的全部功能，并且能够重写父类的功能，实现多态
class Dog(Animal):
    #override
    def run(self):
        print('dog is running...')

    #add
    def eat(self):
        print('eating meat...')

class Cat(Animal):
    def run(self):
        print('cat is running...')

dog = Dog()
dog.run() #当子类与父类拥有同样的方法时，如果实例是子类，那么将自动调用子类的方法，这就是多态
dog.eat()
cat = Cat()
cat.run()

#开边原则：对扩展开放，允许新增子类；对修改封闭，不需要修改依赖类型的函数
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(dog)
run_twice(cat)

#动态语言 vs 静态语言
#对于静态语言java等，如果传入的父类型参数，则传入的对象必须Animal类型或其子类，否则将无法调用
#对于动态语言python，则不一定需要传入Animal类型或其子类，只需要保证传入的对象有一个run方法

#判断对象的类型,type函数返回对应的类型
print(type(123))
print(type(type))

#判断一个对象是否是函数对象,types模块中定义常量FunctionType,BuiltinFunctionType,LambdaType,GeneratorType
import types
def fn():
    pass
r = (type(fn) == types.FunctionType)
print(r)

#判断一个对象是否是类型的实例,isinstance()
a = Animal()
d = Dog()
c = Cat()
ret = isinstance(a,Animal)
print(ret)
ret = isinstance(a,Dog)
print(ret)
ret = isinstance(d,Animal)
print(ret)
ret = isinstance(d,Dog)
print(ret)
ret = isinstance(d,Cat)
print(ret)

ret = isinstance([1,2,2],(list,set,tuple,dict))
print("isinstance",ret)

#使用dir(),如果要获得一个对象的所有属性和方法，使用dir函数，返回一个包含字符串的list
print(dir(d))

#getattr(),setattr(),hasattr()方法用于获取，设置，判断是否存在该属性
ret = hasattr(bart,'name')
print(ret)
setattr(bart,'name','dddddddd')
print(bart.name)
ret = getattr(bart,'name','default') #如果‘name’属性不存在则返回defaul，这样就不会报错
print(ret)

ret = hasattr(d,'run')
print(ret)

#实例属性和类属性
#由于python是动态类型语言，根据类创建的实例可以任意绑定属性
s = Student('bob',90)
s.noattr = 99999
print(s.noattr)

#为class绑定属性，直接在class中定义属性
class Test(object):
    name = 'test' #虽然该属性是类属性，但是所有的实例对象都可以访问该属性

tt = Test()
print(Test.name)
#一个好的习惯是不要让类属性与实例属性名称相同
print(tt.name) #因为实例没有name属性，所以会继续查找class的name属性，但如果实例有name属性，优先选择实例属性
