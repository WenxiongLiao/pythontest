some_sentences = '''I love python
I lovejava
I love C#
'''
f = open('sentence.txt','w',encoding='utf-8')
f.write(some_sentences)
f.close()

f = open('sentence.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if len(line) ==0 :
        break
    print(line)
f.close()

with open('sentence.txt') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)