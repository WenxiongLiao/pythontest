for i in range(1,10):
    print(i)
else:
    print('loop over')

a_list = [1,3,5,7,9]
for i in a_list:
    print(i,end='  ')

a_tuple = (1,3,5,7,9)
for i in a_tuple:
    print(i,end='  ')

a_dict ={'Tom':'1545','jack':'199','juery':'200'}
for key in a_dict:
    print(str(key)+':'+str(a_dict[key]),end='  ')

for key,ele in a_dict.items():
    print(str(key)+':'+str(ele),end='  ')