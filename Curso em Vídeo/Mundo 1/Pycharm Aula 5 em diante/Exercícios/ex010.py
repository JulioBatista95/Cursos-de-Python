n = float(input('Quanto dinheiro você tem na carteira? R$'))
d = n/5.30
print('Você pode comprar US${:.2f} com R${:.2f}'.format(d, n))

w = n/0.0048
print('Você pode comprar W${:.2f} com R${:.2f}'.format(w, n))

e = n/6.40
print('Você pode comprar EU${:.2f} com R${:.2f}'.format(e, n))
