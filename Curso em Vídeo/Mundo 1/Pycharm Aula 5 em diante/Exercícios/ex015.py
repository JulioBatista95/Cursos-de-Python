km = float(input('Quantos km rodados?'))
dias = float(input('Quantos dias de aluguel'))
d = dias*60
c = km*0.15
s = d+c
print('O preço do aluguel é {:.2f}'.format(d))
print('O preço do combustível é {:.2f}'.format(c))
print('logo, o total a pagar é: {:.2f}'.format(s))
