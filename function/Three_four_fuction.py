#无参 无返回
def say_hi():
    print('hi!')

say_hi()
say_hi()

#有参 有返回
def print_sum_two(a,b):
    c = a+b
    return a,b,c

a,b,_ = print_sum_two(4,5)
print(a,b)


x = 60
def foo():
    global  x
    x=3

foo()
print(x)





