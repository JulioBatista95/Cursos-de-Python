#Junior
'''a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número '))
if a > b and a > c:
    print('O maior valor é {}'.format(a))
if b > c and b > a:
    print('O maior valor é {}'.format(b))
if c > a and c > b:
    print('O maior número é {}'.format(c))
if a < b and a < c:
    print('O menor valor é {}'.format(a))
if b < c and b < a:
    print('O menor valor é {}'.format(b))
if c < a and c < b:
    print('O menor valor é {}'.format(c))'''
#Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segunda Valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
