# 输入三个整数x,y,z，请把这三个数由小到大输出。
l = []
for i in range(3):
    j = int(input('输入整数'+str(i)+':'));
    l.append(j)

l.sort()
print(l)

