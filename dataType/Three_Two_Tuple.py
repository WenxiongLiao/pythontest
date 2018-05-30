number_tuple = (1,2,2,4,2,6)
string_tuple = ('abc','bbc','python')
mixed_tuple =('python','java',1,2)
a_tuple = (2,)#需要在后面加,消除歧义

print(number_tuple.count(2))
print(number_tuple)
print(string_tuple)
print(mixed_tuple)
print(a_tuple)

#不能更新也不能删除个别  但是可以删除全部 del mixed_tuple
#mined_tuple[2]='fg'#TypeError: 'tuple' object does not support item assignment
print(mixed_tuple)
print(len(mixed_tuple))#长度
print(number_tuple+string_tuple)#相加
print(number_tuple*3)#相加
print(3 in(number_tuple) ) #判断是否存在
print(number_tuple[1:3])#(2, 2)
print(number_tuple[-3:-1])#(4, 2)
print(number_tuple[2])#2

mixed_tuple=(1,2,['a','b'],3)
print('mixed_tuple:'+ str(mixed_tuple))#mixed_tuple:(1, 2, ['a', 'b'], 3)
mixed_tuple[2][1] = 'c'
print('mixed_tuple:'+ str(mixed_tuple))#mixed_tuple:(1, 2, ['a', 'c'], 3)