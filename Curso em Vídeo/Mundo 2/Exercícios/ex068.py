from random import randint
print('-' * 25)
print('{0:>23}'.format('Jogo do para ou ímpar'))
print('-' * 25)
jogador_pi = computador_pi = ''
numero_jogador = numero_computador = cont = 0
while True:
    jogador_pi = str(input('Escolha [Par/Impar]: ')).upper()
    while True:
        if jogador_pi in 'PAR':
            computador_pi = 'ÍMPAR'
            break
        elif jogador_pi in 'IMPAR':
            computador_pi = 'PAR'
            break
        else:
            print('Opção errada, tente novamente')
            jogador_pi = str(input('Escolha [Par/Impar]: ')).upper()
    print(f'Você escolheu {jogador_pi}')
    print(f'Eu escolhi {computador_pi}')
    numero_jogador = int(input('Escolha um número [Entre 0 e 100]: '))
    numero_computador = randint(0, 100)
    print(f'Eu escolhi {numero_computador}')
    resultado = (numero_jogador + numero_computador) % 2
    soma = numero_computador + numero_jogador
    if jogador_pi in 'PAR':
        if resultado == 0:
            print(f'A soma dos nossos números foi {soma}, que é par.')
            print('Parabéns você venceu! vamos jogar novamente.')
            print('-' * 50)
        else:
            print(f'A soma dos nossos números foi {soma}, que é ímpar.')
            print('Você perdeu, Game Over.')
            break
    else:
        if resultado == 1:
            print(f'A soma dos nossos números foi {soma}, que é ímpar.')
            print('Parabéns você venceu! vamos jogar novamente.')
            print('-' * 50)
        else:
            print(f'A soma dos nossos números foi {soma}, que é par.')
            print('Você perdeu, Game Over.')
            break
    cont += 1
print('Obrigado por jogar.')
print(f'Seu número total de vitórias consecutivas foi {cont}.')
print('Fim')
