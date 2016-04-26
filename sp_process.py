#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#在Thread和Process中，应当优先考虑Process，因为Process更稳定，而且Process可以分布到多台机器山，而Thread最多
#只能在一台机器的多个核心上。

#python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以
#作为调度者，将任务分布到其他子进程中，依靠网络通信。由于managers模块封装的很好，不必了解网络通信的细节，就很容易写
#分布式多进程程序。

#所有的queue只存储在master进程中，worker进程中根本没有创建queue，queue之所以能够通过网络访问，是通过QueueManager
#实现的。由于QueueManager管理的不止一个Queue，所以要为每个queue取个名字，调用接口就能找到指定的queue。

#为了保证两台机器正常的通信，不被其他机器恶意干扰，需要使两台机器的authkey一致。还需要注意，queue的作用是用来传递任务
#和接受结果的，所以每个任务的描述数据尽量要小。

#服务进程，负责启动queue，把queue注册到网络上，然后往queue里面写入任务
import random,time,queue
from multiprocessing.managers import BaseManager

#send tast into queue
task_queue = queue.Queue()
#receive result queue
result_queue = queue.Queue()

#从BaseManager继承QueueManager
class QueueManager(BaseManager):
    pass

#把两个queue注册到网络上，callable参数关联queue对象
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

#绑定端口5000，设置验证码‘ABC’
manager = QueueManager(address=('',5000),authkey=b'abc')

#start queue
manager.start()

#获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去
for i in range(10):
    n = random.randint(0,100000)
    print('put task %d' % n)
    task.put(n)

#从result队列中获取结果
print('try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s' % r)

#关闭
manager.shutdown()
print('manager exit.')
