n1 = 0
cont = 0
total = 0
#Dica: use n1 = cont = total = 0 para diminuir as linhas
n1 = int(input('Digite um número (Digite 999 para interromper): '))
while n1 != 999:
    cont += n1
    #cont += n1 soma todos os números digitados
    total += 1
    #total += 1 faz a contagem de números digitados
    n1 = int(input('Digite um número (Digite 999 para interromper): '))
print('A soma dos números digitados é {}'.format(cont))
print('O total de números digitados foi {}'.format(total))
print('Fim')
