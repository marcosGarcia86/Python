'''
5. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

a = int(input('1º: '))
b = int(input('2º: '))
c = int(input('3º: '))

if a >= b and a >= c:
    print('\t')
    print('1º é maior: %d' %a)
elif b>= c:
    print('\t')
    print('2º é maior: %d' %b)
else:
    print('\t')
    print('3º é maior: %d' %c)

if a <= b and a <= c:
    print('\t')
    print('1º é maenor: %d' %a)
elif b<= c:
    print('\t')
    print('2º é maenor: %d' %b)
else:
    print('\t')
    print('3º é maenor: %d' %c)
