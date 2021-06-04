print('BRASILEIRÃO 2012')
print('-' * 15)
tabela = ('Fluminense', 'Atlético MG', 'Grêmio', 'São Paulo', 'Vasco', 'Corinthians', 'Botafogo', 'Santos',
          'Cruzeiro', 'Internacional', 'Flamerda', 'Náutico', 'Coritiba', 'Ponte Preta', 'Bahia', 'Portuguesa',
          'Sport Recife', 'Palmeiras', 'Atlético GO', 'Figueirense')
print(f'Os 5 primeiros times foram:\n{tabela[0:5]}')
print('-' * 15)
print(f'Os 4 últimos colocados foram:\n{tabela[16:20]}')
print('-' * 15)
print(f'Tabela com os times em ordem alfabética:\n{sorted(tabela)}')
print('-' * 15)
print(f'O time do Fluminense está na {tabela.index("Fluminense")+1}ª posição')