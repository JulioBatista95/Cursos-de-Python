op = produtobarato = ''
total = totmil = cont = precobarato = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        produtobarato = nome
        precobarato = preco
    if preco < precobarato:
        precobarato = preco
        produtobarato = nome
    while op not in 'NS':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        print('-'* 25)
        break
    print('-' * 25)
print(f'O total gasto nesta compra foi {total:.2f}')
print(f'Você comprou {totmil} produtos que custam mais de mil reais.')
print(f'O produto {produtobarato} é o mais barato da compra.')
print('Fim')
