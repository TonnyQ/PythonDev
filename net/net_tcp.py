#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#IP协议:负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，
#然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器
#就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达，
#也不保证顺序到达。IP地址实际上是一个32位整数（称为IPv4），Pv6地址实际上是一个128位整数。

#TCP协议：则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按
#顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，
#就自动重发。

#端口：一个IP包除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
#端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
#每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要
#各自的IP地址和各自的端口号。


#client
import socket

#创建一个socket,AP_INET表示使用IPv4,SOCK_STREAM表示使用面向流的TCP协议
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立connection
sock.connect(('www.sina.com.cn',80))
#send,发送数据;tcp链接创建的双向通道，双方都可以同时给对方发送数据
sock.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#receive,接收数据；
buffer = []
while True:
    #每次最多接收1k字节,调用recv(max)，表示一次最大接收的字节数
    d = sock.recv(1024)
    if d:
        buffer.append(d)
    else:
        break;
data = b''.join(buffer)
print(data)
#关闭连接
sock.close()
