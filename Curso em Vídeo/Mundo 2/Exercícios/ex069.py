idade = maioridade = homens = mulheres = 0
sexo = opcao = ''
while True:
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        maioridade += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        print('-' * 25)
        break
    print('-' * 25)
print(f'O número de pessoas com mais de 18 anos é {maioridade}.')
print(f'O número de homens cadastrados foi {homens}.')
print(f'O número de mulheres com menos de 20 anos cadastradas é {mulheres}.')
print('Fim')
