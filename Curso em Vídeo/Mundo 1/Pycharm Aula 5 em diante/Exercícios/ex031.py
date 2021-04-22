#Junior
d = float(input('Qual a distância da viagem em Km? '))
if d <= 200:
    a = d * 0.5
    print('Você está prestes a começar uma viagem de {}Km.\nE o preço da sua passagem será de R${:.2f} '.format(d, a))
else:
    b = d * 0.45
    print('Você está prestes a começar uma viagem de {}Km.\nE o preço da sua passagem será de R${:.2f} '.format(d, b))
print('Obrigado por usar o aplicativo!')

