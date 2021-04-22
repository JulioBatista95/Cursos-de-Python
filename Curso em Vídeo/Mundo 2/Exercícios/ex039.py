from datetime import date
nascimento = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
d = ano - nascimento
print('''Qual o seu sexo? Responda:
[M] para Masculino
[F] Para Feminino''')
opção = str(input('Sua opção: '))
if opção == 'M':
    if d < 18:
        print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, d, ano))
        print('Ainda faltam {} anos para o seu alistamento'.format((18 - d)))
        print('Seu alistamento será em {}.'.format((nascimento + 18)))
    elif d > 18:
        print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, d, ano))
        print('Você já deveria ter se alistado há {} anos.'.format(d - 18))
        print('Seu alistamento foi em {}.'.format((nascimento + 18)))
    elif d == 18:
        print('Você deve se alistar imediatamente')
else:
    print('O alistamento militar no Brasil, é obrigatório somente para homens.')
