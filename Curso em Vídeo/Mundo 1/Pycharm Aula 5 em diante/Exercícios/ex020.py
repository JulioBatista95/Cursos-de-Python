from random import shuffle
a = input('Primeiro aluno ')
b = input('Segundo aluno ')
c = input('Terceiro aluno ')
d = input('Quarto aluno ')
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
