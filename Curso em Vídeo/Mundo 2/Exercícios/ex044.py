valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista no cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    n1 = valor - (valor * 0.1)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, n1))
elif opcao == 2:
    n2 = valor - (valor * 0.05)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, n2))
elif opcao == 3:
    print('Sua compra custará o valor formal de R${:.2f}'.format(valor))
elif opcao == 4:
    n3 = valor + (valor * 0.2)
    print('Sua compra de R${:.2f} vai custar no final R${:.2f}'.format(valor, n3))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
