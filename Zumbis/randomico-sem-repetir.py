def semRepetir(intervalo, inicial, final):
    import random
    lista = []
    while len(lista) != intervalo:
        x = random.randint(inicial, final)
        if x not in lista:
            lista.append(x)
    #lista.sort()
    print('Lista de %d números aleatórios' % intervalo)
    return (lista)
