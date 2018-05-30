import os
import requests
#1. 自带package和外部package
#     1.1 自带package举例： os; os.getwd()

#2. 外部package以及管理系统介绍: easy_install, pip (comes with Python 3.4)

print(os.getcwd())

r = requests.get('http://www.baidu.com')

print(r.url)
print(r.encoding)
print(r.text)