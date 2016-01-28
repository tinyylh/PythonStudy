#!/usr/bin/python2.7
#coding=UTF-8

#demo.py

import re
DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

for datum in DATA:
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)


print "hello world!"

print 1+2+3

print "你好"

'''
多行注释
'''

print """段落"""

print '单词'

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

str = "asfdasdf,asdfasd"

print str.split(",")

print str.upper()