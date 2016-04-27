#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
#使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。
#UDP传输数据不可靠，优点是速度快.对于不要求可靠到达的数据，就可以使用UDP协议。

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('127.0.0.1',9000))

print('Bind UDP on 9000...')

while True:
    #接收数据
    data,addr = s.recvfrom(1024) #recvfrom返回数据和客户端的地址和端口
    print('Reveived from %s' % addr)
    s.sendto(b'Hello,%s' % data,addr) #sendto，发送数据给客户端


