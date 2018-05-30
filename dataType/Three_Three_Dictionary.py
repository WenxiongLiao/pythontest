# -*- coding: utf-8 -*-
#创建
phone_book = {'Tom':123,'jerry':456}
print(phone_book)
mixed_book = {'Tom':'book','jerry':12.56}
print(mixed_book)

#访问
print('Tom phone munber:'+str(phone_book['Tom']))
#修改
phone_book['Tom']  = 999
print('Tom phone munber:'+str(phone_book['Tom']))
#添加
phone_book['jack']= 888
print('jack phone munber:'+str(phone_book['jack']))

#删除
del phone_book['Tom']
phone_book.clear()
del phone_book

#词典的特性：
#key可以重复
#可以用元组作为键但是不能以列表作为key