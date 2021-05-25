'''lanche = ('hambúrguer', 'suco', 'pizza', 'pudim','Batata Frita', 'Arroz', 'Camarão', 'Jabuticaba')
print(lanche[0])
print(lanche[3])
print(lanche[-2])
print(lanche[0:2])
print(lanche[:1])
print(lanche[2:])
print(lanche[-3:])
print(lanche)

#Tuplas são imutáveis

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer a {comida} na posição {pos}')
#Enumerate mostra o dado e a posição

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba')

#Sorted (Em ordem)
print(sorted(lanche))'''
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(5))
print(c.index(5, 2))'''
pessoa = ('Julio', 26, 'M', 72.00)
print(pessoa)
del(pessoa)
pessoa = ('Maisa', 28, 'F', 43.00)
print(pessoa)
#del(pessoa) ele apaga os dados da variável, podendo ser usada assim como o break, esperando o momento para agir.