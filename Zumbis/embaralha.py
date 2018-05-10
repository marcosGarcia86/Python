'''
defina uma função 'embaralha' que retorne as letras de uma string misturadas.
DICA: utilize list() para converter string em lista
'''

def embaralha(x):
    import random
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)
