'''from random import choice

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
a = int(input("Em que número eu pensei? "))
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
print('O número escolhido foi {}'.format(escolhido))
if a == escolhido:
    print("Parabéns, você acertou!")
else:
    print('Que pena, você errou!')
print('Vamos jogar novamente?')'''

#Os códigos a cima foram feitos por mim, já os de baixo foram feitos na aula

from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador pensar
print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {} '.format(computador, jogador))
