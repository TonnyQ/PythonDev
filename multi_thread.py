#-*- encoding:utf-8 -*-

#进程是由线程组成的，一个进程至少有一个线程；由于线程是操作系统的直接支持执行单元，因此python内置了多线程支持
#python的线程是真实的Posix Thread，而不是模拟出来的线程。

#python对多线程的支持主要为两个模块：_thread低级模块和threading高级模块，threading对_thread进行了封装。
#一般我们主要使用threading模块

#启动一个线程就是把一个函数传入并创建Thread的实例，然后调用start()开始执行:
#由于任何进程默认会创建一个线程，这个线程称之为主线程，主线程又可以启动新的线程，python的threading
#模块有个current_thread()函数，永远返回当前线程实例。

import time,threading
#新的线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)

print('thread %s is runnning...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

#Lock,多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响。而多线程中
#所有的变量都由所有线程共享，所以，任何变量都可以被任何线程修改，因此，线程之间共享数据最大的危险在于对个线程
#同时改一个变量，导致整个程序混乱。

#example0
#假定银行账号的存款
balance = 0

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) #理论上balance=0，但此时balance的值是不确定的，因为balance不能保证数据被同步修改

#为了保证balance计算正确，需要为change_it()函数枷锁，保证同时只有一个线程能够访问并修改balance，
#其他线程等待，知道锁被释放后，获得该锁后才能修改。创建线程锁是通过threading.Lock()实现的.

#example1:Lock
#example0
#假定银行账号的存款
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        #先要获取锁
        lock.acquire() #当多个线程同时请求lock时，只有一个线程能够成功的获取
        try:
            change_it(n)
        finally:
            #释放锁
            lock.release() #获得锁使用完后，必须释放锁，否则其他线程将不会执行，直到锁释放

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) #balance = 0

#result:加锁能够保证数据的安全性，但是加锁阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程执行
#执行效率上就大大减低了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方的锁时，可能造成死锁
#导致多个线程全部挂起，既不执行，也无法结束，直到操作系统强制终止。

#试试python的死循环
import threading,multiprocessing
def loop():
    x = 0
    while True:
        x = x + 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

#python不能完全的占用cpu？因为python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global
#Interpreter Lock，任何python的线程执行前，必须先获得GIL锁，然后，没执行100条字节码，解释器自动释放
#GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有的线程的执行代码都加上锁，所以，多线程在python中只能
#交替执行，即使多核，也只能用到一个核心。所以，python的多线程实际上只能在一个核心上运行，不能充分利用多核的
#优势，然而多进程是能够实现多核任务的。多个python进程各自有独立的GIL锁，互不影响。
