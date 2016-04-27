#asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
#asyncio的编程模型就是一个消息循环。从asyncio模块中直接获取一个EventLoop的引用，
#然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

import asyncio

@asyncio.coroutine
def hexf():
    print('deddddddddddddddddddddddddd')

@asyncio.coroutine #把一个generator标记为coroutine类型，然后把这个coroutine放到Eventloop中
def hello():
    print('Hello,world')
    #异步调用asyncio.sleep
    r = yield from hexf() #此处可以调用别的协程执行
    print('Hello again!')

#获取Eventloop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
print('dedeeeddddddddd')
loop.close()