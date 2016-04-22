#!/usr/bin/env python3

#python内置的一种数据结构，list是一种有序的集合，可以随时添加和删除其中的元素,并且元素可以是不同的数据类型
classmates = ["sss","aaa","ddes",231]
print(classmates)
print("len is ",len(classmates))
print("index 0 is ",classmates[0])#index beyond range,indexerror
print("index -1 is ",classmates[-1])
classmates.append("dses")
print("append : ",classmates)
classmates.insert(1,9999)
print("insert : ",classmates
#classmates.pop()
#print("pop : ",classmates)
#classmates.pop(2)
#print("pop(2) : ",classmates)
#classmates[2] = "Sarah"
#print("replace[2] : ",classmates)
#class0 = [1,1,2,3]
#classmates.append(class0)
#print(classmates)

#tunple一旦初始化就不能修改,能够正常的访问元素，但是不能替换元素，增加，删除元素
#tuple不可修改，能够保证其元素的不变，所以安全也就有保证，能用tuple替代应该尽可能的替代
#students = ("dd","dsd","3333")
#如果元组只有一个数时，就不是元组了
#t = (1) #()也表示数学上的小括号
#t = (1,) #此时t是元组

#可变元组,所谓元组不变，是元组的元素不变，元素的地址不变。
#t = ("a",123,["dd","cc",34])
#print("可变元组 ：",t)
#t[2][0] = "dddddddd"
#print("可变元组 ：",t)





