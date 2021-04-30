print('-' * 40)
print('{0:>23}'.format('Tabuada'))
print('-' * 40)
num = 0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num}  X {c:2} = {num * c}')
    print('-' * 40)
print('Fim')