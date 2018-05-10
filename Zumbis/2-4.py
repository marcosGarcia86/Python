'''
4. Faça um Programa que leia três números e mostre o maior deles.
'''

a = int(input('1º: '))
b = int(input('2º: '))
c = int(input('3º: '))

if a >= b and a >= c:
    print('\t')
    print('1º: %d' %a)
elif b>= c:
    print('\t')
    print('2º: %d' %b)
else:
    print('\t')
    print('3º: %d' %c)
