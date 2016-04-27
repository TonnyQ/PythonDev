#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#urllib模块提供了一系列用于操作URL的功能。
from urllib import request
with request.urlopen('http://www.baidu.com') as f:
    data = f.read()
    print('Statues:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s : %s' % (k,v))
    #print('data: ',data)

req = request.Request("http://www.douban.com/")
req.add_header("User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
with request.urlopen(req) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print("%s:%s" % (k,v))
    print('Data:',f.read().decode('utf-8'))
