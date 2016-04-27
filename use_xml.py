#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

#python处理xml分为两种方式：dom以及sax
#dom:把整个xml文件读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的几点。
#sax:流模式解析，边读边解析，占用内存小，解析快，缺点是需要自己处理事件

#sax解析xml,事件:start_element,end_element,char_data,分别表示节点的开始，内容，节点结束
from xml.parsers.expat import ParserCreate
class DefaultSaxHelper(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s, attrs: %s' % (name,str(attrs)))

    def end_element(self,name):
        print('sax:end_element:%s' % name)

    def char_data(self,text):
        print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHelper()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
