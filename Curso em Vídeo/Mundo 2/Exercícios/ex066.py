n = cont = soma = 0
while True:
    n = int(input('Digite um número [00 para parar]: '))
    if n == 00:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles foi {soma}.')
print('Fim')