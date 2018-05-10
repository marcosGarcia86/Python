'''
verificar se uma palavra é escrita da igual de traz pra frente
'''

word = input('digite uma palavras: ')
if word == word[::-1]:
    print('%s é palíndrome' %word)
else:
    print('%s não é palíndrome' %word)
