print('=-' * 11)
print('Gerador de PA')
print('=-' * 11)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
cont = 1
#O cont irá limitar a quantidade de valores que irá aparecer na tela
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r   #Termo seria o primeiro valor que será somado com a razão
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Fim')
print('Programa finalizado com {} termos mostrados'.format(total))
