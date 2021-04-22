from datetime import date
hoje = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    nascimento = int(input('Digite a {}º data de nascimento: '.format(c)))
    idade = hoje - nascimento
    if idade < 21:
        cont += 1
    elif idade >= 21:
        cont2 += 1
print('')
print('{} pessoas ainda não atingiram a maior idade.'.format(cont))
print('{} pessoas já atingiram a maior idade.'.format(cont2))
