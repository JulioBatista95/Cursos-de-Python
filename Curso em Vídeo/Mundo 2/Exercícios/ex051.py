a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
an = a1 + (9 + 1) * r
for c in range(a1, an, r):
    print('{} '.format(c), end='-> ')
print('Acabou')
