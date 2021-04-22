'''n = int(input('Digite um número: '))
count = 1
resultado = 1
while count <= n:
    resultado *= count
    count += 1
print(resultado)
print(count)'''

# Guanabara
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

n = int(input('Valor: '))
c = n
while c > 0:
