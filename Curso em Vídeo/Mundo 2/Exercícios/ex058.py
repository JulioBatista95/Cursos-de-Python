'''from random import randint
from time import sleep
print('-' * 50)
print('Vou Pensar em um número, você consegue adivinhar?')
print('-' * 50)
computador = randint(0, 10)
jogador = int(input('Qual número estou pensando? '))
chances = 0
print('Processando')
sleep(1)
if computador == jogador:
    print('Parabéns, você venceu! Eu pensei no {} e você também.'.format(computador))
while not jogador == computador:
    computador = randint(0, 10)
    jogador = int(input('Ganhei! eu pensei no número {} e não no {}, tente novamente: '.format(computador, jogador)))
    print('Processando')
    sleep(1)
    if computador == jogador:
        print('parabéns, você venceu! Eu pensei no {} e você também.'.format(computador))
    chances += 1
print('Você precisou jogar {} vez(es) para me vencer!'.format(chances + 1))'''

#Solução

from random import randint
computador = randint(0, 20)
print('Sou seu computador...\nAcabei de pensar em um número de 0 a 20.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
