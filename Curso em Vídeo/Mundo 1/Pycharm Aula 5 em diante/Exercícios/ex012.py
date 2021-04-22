p = float(input('Digite o preço do produto R$ '))
np = (p-(p*0.25))
print('O preço de R${:.2f}, recebeu um desconto de 25%,\ne agora seu novo preço é R${:.2f}'.format(p, np))
