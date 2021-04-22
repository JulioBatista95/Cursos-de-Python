#Junior
'''casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Em quantos anos você pagará pelo empréstimo? '))
mes = tempo * 12
prestacao = casa / mes
if prestacao <= (salario * 0.3):
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado. '
          'Sua prestação ficaria em {:.2f} e, por ultrapassar \n30% do seu salário que é {:.2f}, ele foi negado.'.format(prestacao, (salario*0.3)))'''
#Guanabara
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
