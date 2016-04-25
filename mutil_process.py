#Unix/Linux操作系统提供了一个fork函数，普通函数调用一次，发会一次。但是fork()函数调用一次，返回两次
#因为操作系统自动把当前进程(称为父进程)复制了一份(称为子进程),然后，分别在父进程和子进程内返回。

#子进程永远返回0，而父进程返回子进程的id。理由是，一个父进程可以fork多个子进程，所以，父进程要记下
#每个子进程的id，而子进程只需要调用getppid()就可以拿到父进程的id

#python的os模块封装了常见的系统调用，其中就包括fork，可以在python程序中轻松创建子进程
#由于window没有fork调用，所以fork在window上无效。有了fork调用，一个进程在接到新任务时就可以复制
#一个子进程来处理新任务。
import os
#print('Process (%s) start' % os.getpid())
#pid = os.fork() #仅仅在Unix/Linux/Mac上工作
#if pid == 0:
#    print("i'm child process (%s) and my parent is %s" % (os.getpid(),os.getppid()))
#else:
#    print("I (%s) just created a child process (%s)" % (os.getpid(),pid))

#mutilprocessing,由于python是跨平台的，所以提供了跨平台的多进程模块。
from multiprocessing import Process

#子进程要执行的代码
def run_proc(name):
    print('run child process %s (%s)' % (name,os.getpid()))

#if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc,args=('test',))
#    print('child process will start.')
#    p.start()
#    p.join() #join方法可以等待子进程结束后再继续执行，通常用于进程间同步
#    print('child process end.')


#Pool，如果要创建大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import time,random
def long_time_task(name):
    print('run task %s (%s)' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #设计为最多同时运行4个子进程，只有前面完成了一个子进程，后面的进程才能执行
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocesses done...')
    p.close() #join调用之前必须先调用close，调用close之后就不能继续添加新的process
    p.join()
    print('all subprocesses done.')

#子进程，子进程并不一定是本身，而是外部的进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#subprocess模块可以让我们非常方便的启动一个子进程，然后控制器输入和输出
#import subprocess
#print('$nslookup www.python.org')
#r = subprocess.call(['nslookup','www.python.org'])
#print('Exit code:',r)

#print('$nslookup')
#p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8'))
#print('EXIT CODE:',p.returncode)

#进程间通信，操作系统提供了很多机制来实现进程间通信。python的multiprocessing模块包装了底层的机制，
#提供了Queue,Pipes等多种方式来交换数据.
#window下‘模拟’fork的效果，父进程所以的python对象都必须通过pickle序列化再传到子进程去，所以如果
#multiprocessing在window下调用失败，要先考虑是不是pickle失败了。
from multiprocessing import Queue

#写数据进程执行代码
def write_data(q):
    print('process to write %s' % os.getpid())
    for value in ['a','b','c']:
        print('put %s to queue.' % value)
        q.put(value)
        time.sleep(random.random())

#都数据进程执行代码
def read_data(q):
    print('process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue.' % value)

if __name__ == '__main__':
    #父进程创建Queue，并传给每个子进程
    q = Queue()
    pw = Process(target=write_data,args=(q,))
    pr = Process(target=read_data,args=(q,))
    #启动子进程pw，写入数据
    pw.start()
    #启动子进程pr，读取数据
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程里是死循环，无法等待期结束，只能强制结束
    pr.terminate()
