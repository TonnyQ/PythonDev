#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#simpleclient
import socket

#创建socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
client.connect(('127.0.0.1',8090))
#接收消息
print(client.recv(1024).decode('utf-8'))
for data in [b'Tonny',b'Bob',b'Sam']:
    #发送数据
    client.send(data)
    print(client.recv(1024).decode('utf-8'))
client.send(b'exit')
client.close()
