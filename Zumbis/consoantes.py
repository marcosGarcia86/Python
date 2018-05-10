vet = []
i = 1
while i <=10:
    vet.append(input('letra: '))
    i += 1
i=0
j=0
while i <=9:
    if vet[i] not in 'aeiou':
        j += 1
    i+=1
print ('%d consoantes' %j)
