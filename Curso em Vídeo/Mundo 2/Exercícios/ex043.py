peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura**2)
print('Seu índice de massa corporal (IMC), é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está no seu peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Atenção! Você está obeso.')
elif imc >= 40:
    print('Perigo! Você está com obesidade Mórbida.')
