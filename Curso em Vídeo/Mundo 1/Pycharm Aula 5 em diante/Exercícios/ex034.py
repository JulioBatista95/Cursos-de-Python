#Junior
'''salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    a = (salario * 0.1) + salario
    print('O seu salário de {:.2f}, recebeu um aumento de 10%, e agora ele vale {:.2f}'.format(salario, a))
if salario <= 1250:
    b = (salario * 0.15) + salario
    print('O seu salário de {:.2f}, recebeu um aumento de 15%, e agora ele vale {:.2f}'.format(salario, b))'''

#Guanabara
salário = float(input('Qual o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
