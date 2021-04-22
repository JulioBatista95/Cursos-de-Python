'''ano = int(input('Digite um ano qualquer: '))
e1 = ano % 4
e2 = ano % 100
e3 = ano % 400
if e1 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    if e1 == 0:
        if e2 == 0:
            if e3 == 0:
                print('O número {} é Bissexto'.format(ano))
            else:
                print('O ano {} não é Bissexto'.format(ano))
        else:
            print('O ano {} não é Bissexto'.format(ano))
    else:
        print('O ano {} não é Bissexto'.format(ano))'''

#Guanabara
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
