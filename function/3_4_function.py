#默认参数
def repeat_str(s='xx',times=3):
    repeated_str = s * times
    return repeated_str

repeated_strs = repeat_str('Happy!')#Happy!Happy!Happy!
print(repeated_strs)
repeated_strs = repeat_str('Happy!',2)
print(repeated_strs)#Happy!Happy!

repeated_strs = repeat_str(times = 4,s = 'Happy!')
print(repeated_strs)#Happy!Happy!Happy!Happy!

repeated_strs = repeat_str(4)
print(repeated_strs)#12

#varArgs
#*未指定
#**指定
#先未指定 再指定
def print_paras(fpara,*nums,**words):
    print('fpara:'+str(fpara))#fpara:hello
    print('nums:' + str(nums))#nums:(1, 2, 3, 4, 5, 'C#')
    print('words:' + str(words))#words:{'word': 'python', 'another_word': 'java'}

print_paras('hello',1,2,3,4,5,'C#',word = 'python',another_word = 'java')