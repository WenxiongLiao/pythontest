# -*- coding: utf-8 -*-

print('你好')
print('你好\n我好\n他好')
print(r'你好\n我好\n他好')


#List
#创建list
number_list = [1,2,2,5,7]
print('number_list:'+str(number_list))

number_list = ['test','study']
print('number_list:'+str(number_list))

number_list = [1,2,2.5,0.06,'cdfdfs',2,4,5,7]
print('number_list:'+str(number_list))

#访问元素
print(number_list[0])
print(number_list[0]+number_list[2])
print(number_list[4])

#修改元素
number_list[0] = 15
print(number_list[0])

#删除元素
del number_list[4]
print(number_list)

print(len([1,2,3])) #长度
print([1,2,3]+[4,5,6])  #相加
print(['hello']*4)  #相乘
print(3 in [1,2,3]) #是否存在

abcd_list = ['a','b','c','d']
print(abcd_list[1]) #顺序（从0开始）
print(abcd_list[-2])#倒数第二个（从-1开始）
print(abcd_list[1:])#1到最后
print(abcd_list[1:3])#1到3