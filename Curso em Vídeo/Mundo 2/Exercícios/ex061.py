while
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
while cont <= 10:                                                 #O cont irá limitar a quantidade de valores que irá aparecer na tela
    print('{} -> '.format(termo), end='')
    termo = termo + r                                  #Termo seria o primeiro valor que será somado com a razão
    cont = cont + 1
print('Fim')
