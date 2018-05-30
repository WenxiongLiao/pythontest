import sys
a = 3
b = 4

c = 5.66
d = 8.0

#复数实部与虚部（默认构造方法为浮点型的实部与虚部）
e = complex(c,d)
f = complex(a,b)
print('a is type:',type(a),str(a))
print('b is type:',type(b),str(b))
print('c is type:',type(c),str(c))
print('d is type:',type(d),str(d))
print('e is type:',type(e),str(e))
print('f is type:',type(f),str(f))
print('f is id:',id(f),str(f))
print('\n')

print(a+b)
print(d/c)
print(b/a)
#向下取整
print(b//a)
print(e)
print(e+f)
print(sys.float_info)
