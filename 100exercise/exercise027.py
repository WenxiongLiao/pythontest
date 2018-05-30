# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def out_print(str,lenth):
    if(lenth==0):
        return
    else:
        print(str[lenth - 1])
        out_print(str,lenth-1)

str = input('enter the String:')
out_print(str,len(str))
