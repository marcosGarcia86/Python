arq = open('alice.txt')
txt = arq.read()
txt = txt.lower()

import string
for cont in string.punctuation:
    txt = txt.replace(cont, ' ')
txt = txt.split()

dic = {}
for p in txt:
    if p not in dic:
       dic[p] = 1
    else:
        dic[p] += 1
print('Alice %s vezes' %dic['alice'])
arq.close()
