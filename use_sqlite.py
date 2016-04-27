#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

import sqlite3

#1.连接数据库，如果不存在，则自动在当前目录创建数据库
conn = sqlite3.connect('test.db3')
#2.创建一个Cursor
cursor = conn.cursor()
#3.执行sql语句,创建user表
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#4.继续执行sql语句，插入一条记录
cursor.execute('insert into user (id,name) values(\'1\',\'Tonny\')')
#5.通过rowcount获得插入的行数
print(cursor.rowcount)
#6.执行查询语句
cursor.execute('select * from user where id=?',('1',))
#7.获得查询结果
values = cursor.fetchall()
print(values)
#8.关闭Cursor
cursor.close()
#9.提交事务
conn.commit()
#10.关闭connection
conn.close()

