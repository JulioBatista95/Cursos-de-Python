n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
#Comando break antes da soma para não considerá-lo
    soma += n
    cont += 1
média = soma/cont
print('A soma dos números é {} números'.format(soma))
print(f'Você digitou {cont}')
#f Strings
#print(f'A soma dos números é {soma}')
print(f'Você digitou {cont} números, e a soma deles é {soma}')
print(f'A média desse número é {média:.2f}')
