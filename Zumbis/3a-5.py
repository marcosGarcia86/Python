'''
Dados dois números inteiros positivos, determinar o máximo divisor
comum entre eles usando o algoritmo de Euclides.
EX: mdc(21, 15) = 3
'''

a = int(input('a: '))
b = int(input('b: '))

while a % b != 0:
	a, b = b, a % b

print('mdc = %d' %b)