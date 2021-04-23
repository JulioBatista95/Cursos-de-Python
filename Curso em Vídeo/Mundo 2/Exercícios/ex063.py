#Sequência de Fibonacci -> 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13
print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)
op = int(input('Quantos termos da Sequência de Fibonacci você quer ver? '))
a = 0
b = 1
print('{} -> {}'.format(a, b), end='')
total = 3
while total <= op:
    c = a + b
    total += 1
    a = b
    b = c
    print(' -> {}'.format(c), end='')
print(' -> Fim')