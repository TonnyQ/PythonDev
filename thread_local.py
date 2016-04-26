#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#在多线程环境下，每个线程都由自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有自己线程能够看见
#不会影响其他线程，而全局变量的修改必须加锁，同时还需注意死锁的情况发生。但是，局部变量也有问题，就是函数调用的时候，
#如何传递参数？

#1.使用一个全局的dict来保存数据，然后根据不同的线程id作为key来取值
#2.使用ThreadLocal
import threading
local_school = threading.local() #创建全局ThreadLocal对象

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    print('hello,%s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('alice',),name='thread-a')
t2 = threading.Thread(target=process_thread,args=('bob',),name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()

#全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
#可以把local_school看成全局变量，但是每个属性如local_school.student都是线程的局部变量，可以任意
#的读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理

#result:ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，http请求，用户信息等，这样一个线程的所有调用
#到的处理函数都可以非常方便的访问这些资源。ThreadLocal虽然是个全局变量，但每个线程都只能读写自己线程的副本，互不
#干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
