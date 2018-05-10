def ler():
    arq = open('cripto.txt', 'r')
    for linha in arq.readlines():
        print(linha.rstrip()) #rstrip: retira na leitura
    arq.close()

def escrever():
    import random
    arq = open('msg.txt', 'w')
    for linha in ('aeiouabc'):
        arq.write('%s' % linha)
    arq.close()

def troca():
    msg = open('msg.txt')
    cripto = open('cripto.txt', 'w')
    
    #redlines: lee linha a linha
    for linha in msg.readlines():
        for x in linha:
            if x in 'aeiou':
                cripto.write('*')
            else:
                cripto.write(x)
    msg.close()
    cripto.close()
