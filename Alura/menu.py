from model import perfil

def menu():
    perfil = []
    opcao = ''
    while opcao != 0:
        opcao = input('\n1 - cadastrar\n2 - listar nomes\n0 - sair\n')
        
        if(opcao == '1'):
            perfil(nomes)
        if(opcao == '2'):
            listar(nomes)
        elif(opcao == '0'):
            return ('Fim')
menu()
