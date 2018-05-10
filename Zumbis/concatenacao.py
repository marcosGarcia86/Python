'''
leia uma palavra e troque as vogais por "*"
'''

word = input('digite uma palavra: ')
i = 0
troca = ''
while i < len(word):
    if word[i] in 'aeiou':
        troca += '*'
    else:
        troca += word[i]
    i+=1
print('nova %s' %troca)
