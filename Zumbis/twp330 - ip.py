def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True
arq = open('ips.txt')
correto = open('correto.txt', 'w')
errado = open('errado.txt', 'w')
for linha in arq.readlines():
    if ip_ok(linha):
        correto.write(linha)
    else:
        errado.write(linha)
arq.close()
correto.close()
errado.close()
