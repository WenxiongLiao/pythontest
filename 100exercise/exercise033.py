# 按逗号分隔列表。

L = [1,2,3,4,5]
# print(str(n) for n in L)
s1 = ','.join(str(n) for n in L)
print(s1)


str = '1,2,3,4,5'
print(','.join(str))