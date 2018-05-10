# -*- coding: UTF-8 -*-
'''
pessoas = []

def menu():
    pessoas = []
    opcao = ''
    while opcao != 0:
        opcao = input('\n1 - cadastrar\n2 - listar\n0 - sair\n')
        if(opcao == '1'):
            pessoa(pessoas)
        if(opcao == '2'):
            imprime(pessoas)
        elif(opcao == '0'):
            return ('Fim')
menu()
'''

class perfil(object):
    'classe padrão para perfis'
    def __init__(self, nome, tel, empresa):
         self.nome = nome
         self.tel = tel
         self.empresa = empresa
         self.__curtidas = 0

    def imprimir(self):
        print('Nome: %s\nTelefone: %s\nEmpresa: ' %
              (self.nome.capitalize(), self.tel, self.empresa.capitalize() ))
        
    def curtir(self):
        self.__curtidas+= 1

    def obter_curtidas(self):
        return self.__curtidas

'''---------------------------------perfil vip-------------------------------'''

class perfil_vip(perfil):

    def __init__(self, nome, tel, empresa, apelido):
        super(perfil_vip, self).__init__(nome, tel, empresa)
        self.apelido = apelido

    def credito(self):
        return super(perfil_vip, self).obter_curtidas() * 10.0

'''--------------------------------------------------------------------------'''

class pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float (altura)

    def imprime(self):
        imc = self.peso / (self.altura **2)
        print ('O IMC de %s é: %2.f ' %(self.nome, imc))
