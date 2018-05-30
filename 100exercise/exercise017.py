# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str = input('请输入字符串：')

letters = 0
space = 0
digit = 0
others = 0
for i in range(len(str)):
    c = str[i]
    if(c.isalpha()):
        letters = letters + 1
    elif(c.isdigit()):
        digit = digit + 1
    elif(c.isspace()):
        space = space + 1
    else:others = others + 1

print(letters)
print(digit)
print(space)
print(others)


