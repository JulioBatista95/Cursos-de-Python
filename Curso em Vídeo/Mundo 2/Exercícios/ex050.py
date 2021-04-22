s = 0
cont = 0
for c in range(1, 7):
    a = int(input('Digite {}º valor: '.format(c)))
    if a % 2 == 0:
        s = s + a
        cont = cont + 1
if cont == 0:
    print('Você não digitou nenhum número par, por isso, não foi feito nenhuma soma')
elif cont == 1:
    print('Você digitou {} número par e o resultado da soma é ele mesmo, {}.'.format(cont, s))
else:
    print('Você digitou {} números pares e a soma deles é {}'.format(cont, s))
print('Fim')
