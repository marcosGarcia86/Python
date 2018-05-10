'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.
'''

usuario = input('usuario: ')
senha = input('senha: ')

while usuario == senha:
    print('usuário e senha não podem ser iguais')
    usuario = input('usuario: ')
    senha = input('senha: ')

