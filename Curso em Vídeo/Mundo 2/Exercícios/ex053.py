frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = juntos[::-1]
print('O inverso de {} é {}'.format(juntos, inverso))
if inverso == juntos:
    print('Termos um Palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
