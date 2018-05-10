def ler():
    arq = open('numero.txt', 'r')
    for linha in arq.readlines():
        print(linha.rstrip())
    arq.close()

def lerpy():
    with open('numero.txt') as f:
        print(f.read())
