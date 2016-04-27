#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'tonny',b'Bom']:
    client.sendto(data,('127.0.0.1',9000))
    #接收数据
    print(client.recv(1024).decode('utf-8'))
client.close()
