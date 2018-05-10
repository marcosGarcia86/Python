import urllib.request
import time
# --*-- utf-8 --*--

preço = 99.99
while preço >= 4.65:
    url = 'http://beans.itcarlow.ie/prices-loyalty.html'
    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode('utf-8')
    onde = texto.find('>$')
    ini = onde + 2
    fim = ini + 4
    preço = float(texto[ini:fim])
    if preço >= 4.65:
        time.sleep(100)
print ('compras! preço: %5.2f' %preço)
