'''nome = str(input('Digite seu nome: ')).strip()
if nome == 'Julio':
    print('Que nome bonito você tem {}'.format(nome))
else:
    print('Seu nome é tão normal')
print('Bom dia!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m == 6.0:
    print('Você está na média')
if m > 6.0:
    print('Parabéns você está a cima da média')
if m < 6.0:
    print('Sua média foi ruim')
