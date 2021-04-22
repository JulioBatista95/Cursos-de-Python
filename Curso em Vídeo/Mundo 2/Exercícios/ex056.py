media = 0
maior = 0
for c in range(1, 5):
    print('{}{}ª PESSOA{}'.format('-' * 9, c, '-' * 9))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    media += idade / 4
    if sexo == 'm' or 'M':
        if c == 1:
            maior = idade
        else:
            if idade > maior:
                maior = idade
