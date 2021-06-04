n = 0
while True:
    n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
                 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    n = int(input('Digite um número entre 0 e 20 para ver sua forma por extenso: '))
    if n < 0 or n > 20:
        print('Você digitou o número errado, tente novamente.')
    else:
        break
print(f'Você digitou o número {n_extenso[n]}')
