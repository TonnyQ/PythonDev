#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#ASCII 编码占用一个字节
#Unicode编码占用两个字节
#UTF-8编码为可变长编码，英文字母为一个字节，汉字通常为3个字节，所有字符的编码为1-6字节
#python3版本中，字符窜使用Unicode编码，即python3支持多语言

print("哈哈哈，你好!")

#ord()函数获取字符的整数值，chr()函数获取编码对应的字符
print("哈 = ",ord("哈"))
print("25991 = ",chr(25991))
#print("\u4e2d\u6587 = ",\u4e2d\u6587)

#由于python的字符窜类型是str，在内存中以Unicode编码表示，一个字符对应若干个字节。
#如果要在网络上传输，或者保存在磁盘上就需要把str转换为以字节byte为单位。
#每个byte占用一个字节，以Unicode表示的str通过encode函数可以编码为指定的byte
#如果从网络上或者磁盘上读取字节流，那么读取到的数据就是byte，把bytes转换为str，需要decode

x = b'ABS'
print(x)
print('哈哈'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#计算str包含多少个字符
print("abdddd len is ",len('addddd'))
print("哈哈 len is ",len("哈哈"))


#格式化,在python中采用的格式化和c语言是一致的用%实现
#%d=整数 %f=浮点数 %s=字符串 %x=十六进制整数
#格式化整数和浮点数可以指定是否补0和整数与小数的位数
print('Hello,%s' % 'tonny')
print('hi,%s,you have $%d.' % ('tonny',100000000))
print('%2d-%03d' % (3,1))
print('%.2f' % 3.14159)
print('grown tate: %d %%' % 70)




