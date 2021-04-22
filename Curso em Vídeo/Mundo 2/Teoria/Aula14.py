'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
senhagravada = input('Cadastre uma senha: ')
print('Senha cadastrada com sucesso.')
senha = input('Digite sua senha: ')
while not senha == senhagravada:
    senha = input('Senha errada, digite novamente: ')
print('Olá, seja muito bem vindo!')
print('Deseja recadastrar sua senha?')
r = str(input('[S/N]: ')).strip().upper()[0]
while r not in 'SN':
    r = str(input('Opção errada tente novamente: '))
while r == 'S':
    if r == 'S':
        senhagravada = input('Cadastre uma nova senha: ')
        senha = input('Digite sua senha: ')
        while not senha == senhagravada:
            senha = input('Senha errada, digite novamente: ')
        print('Olá, seja muito bem vindo!')
        print('Deseja recadastrar sua senha?')
        r = str(input('[S/N]: ')).strip().upper()[0]
    elif r == 'N':
        print('Obrigado por cadastrar nossa senha')
print('Obrigado por nos usar.')

s = 0
t = 0
for c in range(1, 6):
    n = int(input('Digite um valor: '))
    if c == 4:                  #Posição
        print('Hey')
    s += n                      #Soma todos os valores
    t += 1                      #Mostra o último valor
print(s)
print(t)
