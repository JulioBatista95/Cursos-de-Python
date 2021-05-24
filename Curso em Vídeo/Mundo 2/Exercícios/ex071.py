print('=' * 40)
print('{0:^40}'.format('Banco JC'))
print('=' * 40)
opcao = int(input('Digite o valor a ser sacado: '))
c = cm = v = vm = d = dm = u = 0
c = opcao // 50
cm = opcao % 50
while True:
    if cm > 0:
        v = cm // 20
        vm = cm % 20
        if vm == 0:
            print('=' * 40)
            break
        else:
            if vm > 0:
                d = vm // 10
                dm = vm % 10
                if dm == 0:
                    print('=' * 40)
                    break
                else:
                    if dm > 0:
                        u = dm // 1
                        print('=' * 40)
                        break
    else:
        print('=' * 40)
        break
print(f'Você precisou de {c} notas de R$50')
print(f'Você precisou de {v} notas de R$20')
print(f'Você precisou de {d} notas de R$10')
print(f'Você precisou de {u} notas de R$1')
print('=' * 40)
print('Fim')