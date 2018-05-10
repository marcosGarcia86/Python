import random

print('**********************\n Jogo da adivinhação!\n**********************')

secreto = random.randint(0,10)
tentativa = 3
#rodada = 1

for rodada in range(1, tentativa +1):
    print('tentativa {} de {}'.format(rodada, tentativa))
    chute = int(input('digite um número: '))
    maior = chute > secreto
    correto = secreto == chute
    print('você digitou ', chute)

    if correto:
        print('\nvocê acertou, nº secreto é %d' %secreto)
        break
    else:
        print('\nchute maior do que o número secreto' if maior
              else '\nchute menor do que o número secreto')

    #rodada = rodada +1
    if tentativa == 0:
        print('suas tentativas terminaram')
print('     fim de jogo! \n**********************')


'''
()
***
* / // %
+ -
'''