#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#datetime模块，是python处理日期和时间的标准库
from datetime import datetime
#获取当前日期和时间
now = datetime.now()
print('Type : %s Content: %s' % (type(now),now))

#获取指定日期和时间
dt = datetime(2015,4,18,12,34,44)
print(dt)

#datetime转timestamp,当前时间相对epochtime的秒数即timestamp
s_count = dt.timestamp()
print("timestamp:",s_count) #python的timestamp是一个浮点数，小数位表示毫秒数

#timestamp转datetime,datetime是有时区概念的，timestamp没有时区的区别
dt = datetime.fromtimestamp(s_count)
print(dt)

#转换为utc时间（格林威治标准时间）
dt2 = datetime.utcfromtimestamp(s_count)
print(dt2)

#str转datetime
cday = datetime.strptime('2015-6-1 18:19:43','%Y-%m-%d %H:%M:%S')
print(cday)

#datetime加减,实际上是往前或者往后推算时间
from datetime import timedelta
forward = now + timedelta(hours=10)
print(forward)
backward = now - timedelta(days=1)
print(backward)

#本地时间转UTC时间，即设定时区时间转标准时间。一个datetime类型有一个时区属性tzinfo=None
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

dj_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt)

#Collections模块，python内建的一个集合模块，提供了许多用用的集合

#1.namedtuple是一个函数，用来创建一个自定义的tuple对象，并规定了tuple元素的个数，并可以用属性而不是索引来
#引用tuple的某个元素，并且具备tuple的不变性。
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple)) #本质上Point是tuple类型的

#2.deque,使用list存储数据时，按索引访问元素很快，但是插入和删除元素很慢，因为list线性存储，数据量大时，
#插入和删除效率很低。deque是为了高效的实现插入和删除的双向列表，适合用于队列和栈.
from collections import deque
q = deque(['a','b',123])
q.append('x')
q.appendleft('r')
print(q)
print(q.pop())
print(q.popleft())
print(q)

#3.defaultdict,使用dict时，如果引用的key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值
#可以使用defaultdict.默认值并不存在于dict中，而是通过函数返回的，即defaultdict与dict其他行为完全一样。
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'ads'
dd['eee'] = 1233
print(dd)
print(dd['eee'])
print(dd['e2']) #if key no exit,return N/A default value

#4.OrderedDict，使用dict时，Key是无序的。对dict做迭代时，无法确定key的顺序。如果要保证key的顺序，
#可以使用OrderedDict.使用OrderedDict的key顺序是按插入顺序的。
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('c',1),('b',2),('a',3)]) #有序，按添加顺序，并不是按key排序
print(od)

#5.Counter,一个简单的计数器,Counter实际上也是dict的一个子类。
from collections import Counter
c = Counter()
for ch in 'aaaabbbsds':
    c[ch] = c[ch] + 1
print(c)

#Base64,是一种用64个字符来表示任意二进制数据的方法。Base64是一种最常见的二进制编码方法。
#base64不能用于加密，适用于小段内容的编码
#Base64原理：
#1.首先，需要确定一个使用的64个字符的数组；
#2.然后，对二进制数据进行处理，每3个字节一组，一共是3*8=24bit，划分为4组，每组正好6bit；
#3.得到4个数字作为索引，然后查表，获得相应的4个字符，这就是编码后的字符串。
#4.base64编码会把3个字节的二进制数据编码为4个字节的文本数据，长度增加33%。
#5.如果要编码的二进制数据不是3的倍数，最后剩下1或2个字节？Base64采用\x00字节在末尾补足，再在编码的末尾加上1或2个’=’，表示补了多少位字节。
import base64
e = base64.b64encode(b'binary\x00string')
print(e)
d = base64.b64decode(e)
print(d)
#由于标准的base64编码后可能出现字符‘+’或’/’，在url中就不能直接作为参数，所以可以采用url-safe的base64
#编码，其实就是将‘+’和‘-’变为’-‘和’_’.
e = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)
e = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)
d = base64.urlsafe_b64decode(e)
print(d)

#struct,python并没有专门处理字节的数据类型，但是由于str既是字符串，又可以表示字节。所有str==字节数组。
#python提供了struct模块来解决bytes和其他二进制数据类型的转换，性能要求不高时，可以使用struct。
import struct
#struct的pack函数能把任意数据类型转换为bytes
r = struct.pack('>I',10240099) #'>'表示字节顺序是big-endian,也就是网络字节序，I表示4个字节无符号整数
print(r)
#struct的unpack函数把bytes转换对应的数据类型
r = struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
print(r)#'>IH'表示后面的bytes一次变为I：4个字节无符号整数和H：2个字节无符号整数

#hashlib,提供常见的摘要算法，md5，sha1等等。
#哈希算法，通过一个函数，把任意长的数据转换为一个长度固定的数据串（通常是16进制的字符串表示）.
import hashlib
#1.md5,生成固定的128bit字节，通常用一个32为的16进制字符串表示。
md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('how to use md5 in python '.encode('utf-8'))
md5.update('hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#2.SHA1,用160bit字节们通常用40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python '.encode('utf-8'))
sha1.update('hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#itertools,提供了用于操作迭代对象的函数。
import itertools
#count:无限迭代
natuals = itertools.count(1)
#for n in natuals:
#    print(n)

#cycle(),会把传入的一个序列无限重复下去。
cs = itertools.cycle('abc')
#for c in cs:
#    print(c)

#repeat(),负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('a',3)
for n in ns:
    print(n)

#takewhile()函数根据条件判断来截取一个优先序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x <= 10,natuals)
l = list(ns)
print(l)

#chain(),可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('abc','xyz'):
    print(c)

#groupby(),把迭代器中相邻的重复元素跳出来放在一起：
for key,group in itertools.groupby('AAAbbbdddaa',lambda c:c.upper()):
    print(key,list(group))
