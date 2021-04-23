n1 = 0
cont = 0
total = 1
while n1 != 999:
    n1 = int(input('Digite um número: '))
    cont += n1
    total *= cont
print(cont - 999)
print(total)
print('Fim')
