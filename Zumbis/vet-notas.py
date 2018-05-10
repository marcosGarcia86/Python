vet = []
i=1
while i <=4:
    nota = int(input('digita a %d nota: ' % i))
    vet.append(nota)
    i += 1
media = 0
i = 0
while i <= 3:
    media += vet[i]
    i += 1
print('notas', vet)
print('media %.2f' % (media/4))
