#!/usr/bin/env python3

print("hello,python")

#mutil args output
print("a","ddd","2222",100 +200)

#input 
name = input("please enter your name:")
print(name)

#origin char
print("\\\t\\")
print(r"\\\t\\")
print("""line1
	line2
	line3""")

#and or not
print(True and True)
print(True and False)
print(False and False)
print((5 > 3 and (3 > 1)))

print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not False)

# None不是0，None是一个特殊的空值
print(None)

# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123
print("a = ",a)
a = "ABS"
print("a = ",a)

# 理解python的动态类型
a = 456
print("a id is :",id(a))
b = a
print("b id is :",id(b))
a = "str"
print("a id is :",id(a))
print("b id is :",id(b))

# 理解python的常量，常量就是不能变得变量
PI = 3.14 #此时PI任然是一个变量，python并没有提供任何机制保证常量

# python的除法,"/" and "//"
print(10/3)    #浮点除法，商为浮点值
print(10 // 3) #地板除法，商为整数
