'''
faça um programa que leia um vetor de numeros reais e mostre-os na ordem
inversa
'''

vetor = []
i=1

while i <= 5:
    x = int(input('digite um número: '))
    vetor.append(x)
    i += 1
i=4
while i >= 0:
    print(vetor[i])
    i -= 1
