#!/usr/bin/env python3

# 调用函数,如果传入的参数数量不对，会报TypeError
print("abs(-100) is %s" % abs(-100))

#数据类型的转换,python3内置的常用函数包括数据类型转换函数
print(int("123"))
print(int(12.34))
print(float("12.443"))
print(str(1232))
print(bool(212))

#函数名其实就是一个指向函数对象的引用，完全可以把函数名赋给一个变量，相当于给函数起了别名
a = abs
a(-1)

#定义函数,在python中定义一个函数使用def关键字,如果函数没有没有明确的return，则会返回一个None
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bas operand type.")

    if(x > 0):
        return x
    else:
        return -x

print("my_abs(-100) is %s" % my_abs(-100))

#空函数,pass语句表示什么也不做，实际上pass可以用来作为占位符。
def nop():
    pass

print(nop())

age = 20
if age > 18:
    pass

#参数检查，调用函数时，如果函数参数个数不对，python解释器会自动检查出来,但是如果是参数类型错误，则检查不出来
#my_abs(1,2)
#my_abs("ddd")

#多个值返回，在python中实际上是返回一个元组
def my_mod(a,b):
    x = a % b
    y = (a // b)
    return (x,y)
x,y = my_mod(14,6)
print(x,y)

#函数的参数,默认参数、可变参数、关键字参数

def powern(x,n = 2): #n为默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = (s * x)
    return s
print(powern(5,4))
print(powern(5))
#默认参数可以简化函数的调用，设置默认参数时，需要注意一下几点：
#1.必选参数在前，默认参数在后，否则python的解释器会报错
#2.如何设置默认参数？当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数可以作为默认参数
#3.有多个默认参数时，调用的时候，即可以按顺序提供默认参数，也可以不按顺序提供，但是此时需要把参数名指出
print(powern(4,n = 8))

#使用默认参数时务必小心:默认参数必须指向不可变对象
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())

#可变长参数,在python函数中，可以定义可变长参数。可变参数就是传入的参数个数是可变的。
#参数numbers前添加了*，参数numbers接受的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + (n * n)
    return sum

print(calc(2,3,43,4))
print(calc(2,3,43,3,4,5,4,4))

#但是如果参数中已经包含了一个list或者tuple，要调用一个可变参数怎么办？
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
#但是这么写相当的繁琐,python允许在你的list或者tuple前面加一个*，把list或者tuple的元素转成可变参数
a = calc(*nums)
print(a)

#关键字参数，可变参数允许你传入0或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为dict
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

person("tonny",26)
person("box",23,city="beijing")
person("Ams",22,gender="M",job="Engineer")

#关键字参数有什么用？可以扩展函数的功能。
extra = {"city":"Beijing","job":"enginn"}
person("jack",23,**extra)

#命名关键字参数,对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
def person2(name,age,**kw):
    if "city" in kw:
        pass
    if "job" in kw:
        pass
    print("name",name,"age",age,"other",kw)

person2("jack",222,city="beigji",addr="chaoyang",zipcode=12333)

#和关键字参数**kw不同，命名关键字参数需要一个特殊的分隔符*,*后面的参数被视为命名关键字参数
#命名关键字参数可以有缺省值
def person3(name,age,*,city="beijing",job):
    print(name,age,city,job)

person3("jac",2,city="be",job="en")
person3("jac",2,job="en")
#命名关键字参数必须传入参数名，这和位置参数不同，如果没有传入参数名，调用会出错；
#python解释器认为这四个参数都是位置参数，但是person3只接受两个位置参数
#person3("jac",2,"be","en")

#参数组合，在python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数、命名关键字参数。
#这五种参数可以组合使用。除了可变参数无法和命名关键字参数混合。但请注意，参数定义的顺序必须是
#必选参数、默认参数、可变参数|命名关键字参数和关键字参数

#递归函数，在函数内部，可以调用其他函数。如果在一个函数内部调用自身，这个函数就是递归函数。
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈这种数据结构实现的，没当进入一个函数调用，
#栈就会加一层栈帧，没当函数返回，栈就会减少一层栈帧。由于栈的大小不是无限的。所以递归调用的次数过多，会
#导致栈溢出。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(100))

def facts(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num -1,num * product)

#print(fact(1000))
print(facts(100))
