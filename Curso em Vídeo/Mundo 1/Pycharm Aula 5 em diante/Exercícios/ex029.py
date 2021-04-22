'''velocidade = float(input('Qual a velocidade do carro? '))
a = velocidade - 80
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Sua velocidade foi de {}km/h ultrapassando a velocidade máxima de 80 km/h em {} km/h, por isso,\n'
          'foi multado em R$ 7.00 para cada km ultrapassado, resultando\n'
          'em um valor de {} reais'.format(velocidade, a, multa))
if velocidade <= 80:
    print('Sua velocidade está a baixo da máxima permitida.')'''
#Junior

#Guanabara
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
