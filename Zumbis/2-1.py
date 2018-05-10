'''
1. Faça um Programa que peça os três lados de um triângulo. O programa
deverá informar se os valores podem ser um triângulo. Indique, caso os
lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

a1 = int(input('insira a area: '))
a2 = int(input('insira a altura: '))
a3 = int(input('insira a base: '))

if a1 > a2 + a3 or a2 > a1 + a3 or a3 > a1 + a2:
    print('não é triangulo')
elif a1 == a2 == a3:
    print('triangulo equilatero')
elif a1 == a2 or a2 == a3 or a1 == a3:
    print ('triangulo isosceles')
else:
    print('triangulo escaleno')
