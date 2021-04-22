from time import sleep

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0

while not opcao == 5:
    sleep(1.3)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre o número {} e o número {} é {}.'.format(n1, n2, soma) )
    elif opcao == 2:
        multiplicar = n1 * n2
        print('A multiplicação do número {} com o número {} é {}.'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}.'.format(n2, n1))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Fim')
    elif opcao > 5:
        print('Opção inválida, tente novamente.')
print('Obrigado por usar nosso aplicativo')