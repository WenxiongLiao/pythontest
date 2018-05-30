# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 输出所有回文数

def is_hui(num):
    w = int(num/10000)
    q = int(num%10000/1000)
    s = int(num%100/10)
    g = int(num%10)

    if(w==g and q==s):
        return  1
    else:
        return 0


for i in range(10000,99999):
    if is_hui(i)==1:
        print(i)