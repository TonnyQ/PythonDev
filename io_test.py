#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#IO编程中，Stream是一个很重要的概念，InputStream就是数据从外面（网络，磁盘）流进内存，
#OutputStream就是数据流从内存流到外面。

#同步与异步：
#CPU等待执行，等任务完成后再执行，称为同步IO
#CPU不等待，继续执行后续任务，称为异IO
#异步的通知模式：回调与轮询

#python中内置了读文件的函数，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）
#然后，通过操作系统提供的接口从这个文件对象中读取数据(读文件),或者把数据写入这个文件对象。

#open(path,mode):path,文件路径，mode,文件访问方式，‘r’为读取;
#如果文件不存在，open函数会抛出IOError错误，并给出错误码和详细信息
try:
    f = open(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt','r')
    s = f.read();
    print(s)
except BaseException as e:
    print('io error :',e)
finally: #使用finally保证及时出错也能及时关闭文件流
    f.close() #关闭文件流，文件使用完毕必须关闭因为文件对象会占用操作系统资源，并且操作系统同时只能打开的文件数量是有限的

#python引入with语句简化调用close()方法
with open(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt','r') as f:
    print("with :",f.read())

#调用read方法会一次性的读取文件中所有的内容，如果文件非常大，可能在低内存的机器上占满内存。
#所以为了安全，可以使用read(size)方法，或者使用readline读取一行，另外还能调用readlines
#读取多行，返回一个list。根据实际情况，如果文件很小，可以使用read,不能确定大小多次使用read(size)
#如果是配置文件，则调用readlines最方便。


#file-like object：像open函数返回的这种有个read方法的对象，在python中统称为file-like对象。
#除了file外，还有网络、字节流、自定义流。file-like object不要求特定类继承，只要包含read方法。
#例如StringIO就是在内存中创建的file-like object,常用做临时缓冲区


#二进制文件,之前的读取模式读取的都是文本文件，并且编码默认为utf-8，但是要读取二进制文件，比如图片等
#文件，需要使用‘rb’模式打开文件流
with open(r"C:\Users\Tonny\Pictures\fuzi.jpg",'rb') as f:
    f.read()

#字符编码：要读取非utf-8文本文件，需要给open函数传入参数encoding参数。
f = open(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt','r',encoding='gbk')

#写文件,和读文件一样，唯一的区别是open函数的打开模式变为‘w’或者‘wb’表示写入文本文件或者二进制文件。
#当我们写文件时，操作系统往往不会立即把数据写入磁盘，而是放到内存中缓冲起来，空闲的时候再写入磁盘，只有调用
#close()方法时，操作系统才保证把没写入的数据全部写入磁盘。所以，必须在写完后关闭文件流。
f = open(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt','w')
f.write('heello,worldddd!!!')
f.close()

#StringIO,很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO就是在内存中读写str。
from io import StringIO
f = StringIO()
l = f.write('heelllllllll')
print('write length : ',l)
l = f.write('ddd')
print('write length : ',l)
print(f.getvalue()) #getvalue(),用于获取写入后的str
f.close()

#读取StringIO，可以用一个str初始化StringIO，然后想读文件一样读取：
f = StringIO('hello,\njdejd')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
f.close()


#StringIO操作的只能是str，如果需要操作二进制数据，就需要BytesIO;BytesIO实现了在内存中读写bytes。
from io import BytesIO
f = BytesIO()
l = f.write('我是谁？'.encode('utf-8')) #此时写入的不是字符串，而是转换后的bytes
print(l)
print(f.getvalue())
f.close()

f = BytesIO(b'\xe6\x88\x91\xe6\x98\xaf\xe8\xb0\x81\xef\xbc\x9f')
s = f.read()
print(s)

#操作文件和目录，在python内置模块os中包含了直接调用操作系统操作文件以及目录的接口。
import os
print(os.name) #操作系统的类型nt,uname()函数不再window上提供，也就是说os模块中的方法跟操作系统相关

#环境变量,在操作系统中定义环境变量，全部保存在os.environ变量中，可以直接查看
print(os.environ)
print(os.environ.get('path'))

#操作文件和目录,os,os.path

#查看当前目录的绝对路径
s = os.path.abspath('.')
print(s)

#在某个目录下创建一个新的目录，首先把新目录的完整路径表示出来：把两个路径合并时，使用join方法，可以正确的跨平台处理路径分隔符
s = os.path.join(r'C:\Users\Tonny\Documents\GitHub\PythonDev','testdir')
print(s)

#根据生成的路径，真实的创建目录
os.mkdir(s)

#删除创建的目录
os.rmdir(s)

#拆分文件路径，os.path.split()以及os.path.splitext(),合并，拆分仅仅是对字符串的操作，并不要求目录真实存在
print(os.path.split(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt'))
print(os.path.splitext(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt'))

#文件操作
#对文件重命名
os.rename('test.txt','test.py')

#删除文件
os.remove('test.py')

#复制文件,os模块并没有复制文件的功能，原因是操作系统不提供文件复制的功能。理论上我们能够通过文件读写完成
#文件的复制。在shutil模块中提供了copyfile()函数

#利用python的特性过滤文件。
lis = [x for x in os.listdir('.') if os.path.isdir(x)]
print(lis)


