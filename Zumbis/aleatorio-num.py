def aleatorio(intervalo, inicial, final):
    import random
    lista = []
    for i in range(intervalo):
        lista.append(random.randint(inicial, final))
    #lista.sort()
    return (lista)
