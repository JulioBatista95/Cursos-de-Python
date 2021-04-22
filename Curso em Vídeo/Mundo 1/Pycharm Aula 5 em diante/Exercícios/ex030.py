#Identificamos se um número é par ou ímpar quando o dividimos por dois.
#Se o resto da divisão for zero, o número é par; caso contrário, é ímpar.
#Junior
'''numero = int(input('Digite um número: '))
r = numero % 2
if r == 0:
    print('O número {} é par'.format(numero))
if r != 0:
    print('O número {} é ímpar'.format(numero))'''

#Guanabara
número = int(input('Me diga um número qualquer:'))
resultado = número % 2
if resultado == 0:
    print('O número {} é par'.format(número))
else:
    print('O número {} é ímpar'.format(número))
