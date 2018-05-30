i = 5
print('i:'+str(i))

for i in range(1,10):
    for j in range(1,i+1):
        print('\t'+str(i)+'*'+str(j)+'='+str(i*j),end='')
    print('\n')