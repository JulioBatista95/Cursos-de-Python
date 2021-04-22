from datetime import date
nascimento = int(input('Qual a data de nascimento do nadador? '))
atual = date.today().year
idade = atual - nascimento
print('Sua idade atual é de {} anos.'.format(idade))
print('Por isso')
if idade <= 9:
    print('Sua categoria é a MIRIM')
elif 10 <= idade <= 14:
    print('Sua categoria é a INFANTIL')
elif 15 <= idade <= 19:
    print('Sua categoria é a JUNIOR')
elif 20 <= idade <= 25:
    print('Sua categoria é a SÊNIOR')
elif idade > 25:
    print('Sua categoria é a MASTER')
