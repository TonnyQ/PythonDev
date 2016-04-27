#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
#如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
#所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。
#由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
#一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
#但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，
#否则，服务器一次就只能服务一个客户端了。

#simpleserver

import socket
import threading,time

def tcplink(sock,addr):
    print('Accept new connection from %s:%s' % (sock,addr))
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break;
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s' % (sock,addr))

def createServer():   
    #创建socket
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定监听端口
    server.bind(('127.0.0.1',8090))
    #监听listen
    server.listen(5)
    print('Waiting for connection...')

    while True:
        #接收一个新的连接
        sock,addr = server.accept()
        #创建新线程来处理tcp连接
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()

if __name__ == '__main__':
    createServer()
