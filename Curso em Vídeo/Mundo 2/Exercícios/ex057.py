sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Tente novamente: ')).strip().upper()[0]
print('Sexo {}, registrado com sucesso'.format(sexo))
