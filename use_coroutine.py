#协程，又称为微线程(Coroutine)
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
#协程是在一个线程中执行。最大的优势是协程具有极高的执行效率。没有线程切换的开销，和多线程相比，线程数量越多，协程的性能优势越明显
#并且协程不需要枷锁，因为只有一个线程，也不存在同时写变量的冲突，在协程中控制共享资源不加锁，只需要判断状态就好了。

#在python中协程是通过generator实现的。可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
#Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consumering %s...' % n)
        r = '200,0K'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

