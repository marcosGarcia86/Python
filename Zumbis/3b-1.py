'''
Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um
inteiro não-negativo n, verificar se n é triangular.
'''
x = int(input('x: '))
j = 0
while j *(j+1) * (j+2) < x:
    j = j + 1
print(j * (j+1) * (j + 2) == x)
