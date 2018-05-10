arq = open('numero.txt', 'w')
for linha in range (1, 51):
    arq.write('%d\n' % linha)
arq.close()
