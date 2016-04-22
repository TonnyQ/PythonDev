#!/usr/bin/env python3

#python内置字典：dict的支持，使用key-value存储，具有极快的查找速度.
dic = {"michael":977,"Bob":322,"Tonny":1000}
print(dic["Tonny"])

dic["Adm"] = 999
print(dic)

dic["Adm"] = 990 #一个key只能对应一个value，所以adm对应于990
print(dic)

#访问一个不存在的key将会产生一个异常
#d["abc"]

#避免key不存在的错误，一种办法是通过in关键字判断key是否存在
#二是通过dict的get方法访问，如果key不存在，返回None，或者自己指定value.
print("dic has Tonny. key : %s" % "Tonny" in dic)
print("dic has Tonny. Key2: %s" % dic.get("Tonny",-1)) #返回None时python交互命令下不显示结果

#dict删除一个key-value
dic.pop("Adm")
print("pop adm key : %s" % dic)

#dict内部存放的顺序与key放入的顺序无关
#和list比较，dict有以下几个特点：
#	1.查找和插入的速度极快，不会随着key的增加而变慢
#	2.需要占用大量的内存，内存浪费多
#而list相反:
#	1.查找速度和插入的时间随元素的增加而增加
#	2.占用空间小，浪费内存小
#dict能够用于需要高效查找的情况中，但是需要记住dict的key必须是不可变对象.这是因为dict
#根据key来计算value的内存地址，如果每次计算的key的值都不同，dict的值就不正确了，其实是计算hash
#在python中字符窜、整数、元组都是不可变对象，可以放心的作为key，而list可变，不能用于key

#set和dict类似，也是一组key的集合，但不存储value，由于key也不能重读，所以set中，没有重复的key
s = set([1,2,4])
print(str(s)) #set显示顺序不一定与出入参数顺序一致

ass = set([1,2,1,1,2,1,4])
print(str(ass))
#重复元素将被set自动过滤

#通过add(key)方法添加元素到set中，可以重复添加，但不会产生效果.
ass.add(4)
ass.add(4)
print(ass)

#也可以通过remove(key)移除set中的元素
ass.remove(4)
print(ass)

#set可以看做数学意义上的无序和无重复的集合，因此可以做数学意义上的交集、并集等操作
s1 = set([1,2,4])
s2 = set([2,3,5])
print("s1 & s2 is %s" % (s1 & s2))
print("s1 | s2 is %s" % (s1 | s2))

#set和dict的唯一区别在于没有存储对应的value，但是set的原理和dict一样，同样不可以放入可变对象
#因为无法判断两个可变对象是否相等，也就无法保证set内部元素是否相等。
#对于不可变对象，调用自身的任意方法，也不会改变该对象自身的内容。相反，这些内容会创建新的对象
#并返回，这样就保证了不可变对象的本身永远是不可变的。

#由于第二个元素包含一个list，而list是可变的。所以包含可变元素的元组不能作为key
#dicss = {(1,1,2):"tupl1",(1,2,[3,4]):"tupl2"}
dicss = {(1,2,3):"tuple"}
print(dicss)
