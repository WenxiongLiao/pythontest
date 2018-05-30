try:
    int1 = int(input("enter an int:"))
    print(0/0)

except ValueError:
    print('只能输入整数')
except EOFError:
    print('读到文件尾')
except:
    print('除数不能为0')