s = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        s += c
print('O somatório de todos os números ímpares múltiplos de 3 foi {}'.format(s))
print('Fim!')

#Guanabara
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os valores {} solicitados é {}'.format(cont, soma))
