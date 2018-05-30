for i in range(1,5):
    print(i,end=' ')#1 2 3 4

for i in range(1,10,2):
    print(i,end=' ')# 1 3 5 7 9

print('\n')
for i in range(1,10):
    for j in range(1,i+1):
        print('\t'+str(i)+'*'+str(j)+'='+str(i*j), end='')
    print('\n')