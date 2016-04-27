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
