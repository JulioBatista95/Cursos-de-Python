a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
m = (a + b) / 2
print('Sua média foi {:.2f}'.format(m))
if m < 5:
    print('Média abaixo de 5.0: Reprovado')
elif 5 <= m <= 6.9:
    print('Média entre 5.0 e 6.9: Recuperação')
elif m >= 7:
    print('Média igual ou superior a 7: Aprovado')
