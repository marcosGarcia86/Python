# -*- coding: UTF-8 -*-
import re

def numRand():
    import random
    ''' from random import randint, irá importar somente o método
randint da biblioteca random '''

    aleatorio = random.randint(1,100)
    while True:
        chute = int(input('Chute um número: '))
        if chute == aleatorio:
            print ('Você venceu! Nº correto é %d' %aleatorio)
            break
        else:
            print('chute Alto' if chute > aleatorio else 'chute baixo')
    return('Fim de jogo!')    

def randNome():
    # -*- coding: UTF-8 -*-
    import csv, sys, os, codecs, random
    
    with open('arquivos.csv', 'r', encoding='iso-8859-1') as f:
        r = csv.reader(f.readlines())
        for linha in r:
            random.choice(linha)
            print (linha[0])
'''
def lerPd():
    import PyPDF2

        return (content)
'''
def convite(conv):
    tamanho = len(conv)
    fim = len(conv)
    ini = fim - 4
    part2 = conv[ini:fim]
    part1 = conv[0:4]
    return ('o codigo gerado foi: %s %s' %(part1.lower().capitalize(),
                                           part2.lower().capitalize()))


nomes = []

def cadastrar(nomes):
    print('nome: ')
    nome = input()
    nomes.append(nome)

def listar(nomes):
    print('listar nomes:')
    for nome in nomes:
        print(nome.capitalize())
'''
def menu():
    nomes = []
    opcao = ''
    while opcao != 0:
        opcao = input('\n1 - cadastrar\n2 - listar nomes\n0 - sair\n')
        
        if(opcao == '1'):
            cadastrar(nomes)
        if(opcao == '2'):
            listar(nomes)
        elif(opcao == '0'):
            return ('Fim')
menu()
'''

def gera(nomes):
    posicao_final = len(nomes)
    posicao_inicial = posicao_final - 4
    parte1 = nomes[0:4]
    parte2 = nomes[posicao_inicial :posicao_final]
    print ("%s %s" %(parte1, parte2))
    return ('Enviando convite para %s ' % (nomes))

def procurar_regex(nomes):
    print('Digite a expressão regular:')
    regex = input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)
