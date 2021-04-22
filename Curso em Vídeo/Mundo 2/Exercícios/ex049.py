a = int(input('Digite um número: '))
for c in range(1, 11):
    d = a * c
    print(a, 'x', c, '=', d)

#Guanabara
num = int(input('Digite um número para conferir sua tabuada: '))
for c in range(1, 11):
    print('{}  x  {:2} = {}'.format(num, c, num * c))
