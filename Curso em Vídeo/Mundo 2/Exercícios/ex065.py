op = ''
m = cont = maior = menor = 0
while op != 'N':
    n1 = int(input('Digite um número: '))
    cont += n1
    m += 1
    if m == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
média = cont / m
print('Você digitou {} números e a média entre todos os valores digitados é {:.2f}'.format(m, média))
print('O maior número que você digitou é {} e o menor é {}.'.format(maior, menor))
print('Fim')