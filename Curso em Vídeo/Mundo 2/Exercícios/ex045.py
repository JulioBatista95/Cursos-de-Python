import random
from time import sleep
print('{:=^40}'.format(' Vamos Jogar Jokenpô '))
print('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('--> '))
if opcao > 3:
    print('Você escolheu a opção errada, tente novamente.')
if opcao == 1:
    b = 'Pedra'
elif opcao == 2:
    b = 'Papel'
elif opcao == 3:
    b = 'Tesoura'
computador = random.randint(1, 3)
if computador == 1:
    a = 'Pedra'
elif computador == 2:
    a = 'Papel'
elif computador == 3:
    a = 'Tesoura'
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PÔ!!!')
sleep(0.75)
print('=-'*15)
if opcao == computador:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(a))
    print('=-' * 15)
    print('EMPATE')
elif opcao == 1 and computador == 2:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O COMPUTADOR VENCEU!')
elif opcao == 1 and computador == 3:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O JOGADOR VENCEU!')
elif opcao == 2 and computador == 1:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O JOGADOR VENCEU!')
elif opcao == 2 and computador == 3:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O COMPUTADOR VENCEU!')
elif opcao == 3 and computador == 1:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O COMPUTADOR VENCEU!')
elif opcao == 3 and computador == 2:
    print('O computador jogou {}'.format(a))
    print('O jogador jogou {}'.format(b))
    print('=-' * 15)
    print('O JOGADOR VENCEU!')