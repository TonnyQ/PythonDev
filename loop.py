#!/usr/bin/env python3

#python的循环有两种，一种是for..in循环依次把list或者tuple元素迭代出来
names = ["aaa","dsese","deeeeeee"]
for name in names:
	print(name)

#求和
sum = 0
for x in [1,2,3,4,222,5,4,3,433]:
	sum = sum + x
print("sum = ",sum)

#range函数,可以生成一个整数序列在通过工厂方法list()转换成list
a = list(range(100))
sum = 0
for x in a:
	sum = sum + x
print("Range(100) sum is ",sum)

#python的第二种循环是while，只要条件满足就循环，否则退出循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print("while sum is ",sum)


