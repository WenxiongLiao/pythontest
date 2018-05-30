# 题目：利用递归方法求5!。

def fact(j):
    sum =1;
    if(j==1):
        sum=1
    else:
        sum = fact(j-1) * j

    return sum;


print(fact(5))


