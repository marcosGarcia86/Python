vet = []
media = 0
i = 1
while i <= 4:
    nota = int(input('digita a %d nota: '))
    vet.append(nota)
    media += nota
    i += 1
print('notas', vet)
print('media %.2f' % (media/4))
