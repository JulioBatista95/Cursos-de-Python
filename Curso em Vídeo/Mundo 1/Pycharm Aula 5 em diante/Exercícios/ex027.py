n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))
# para identificar o último nome A função -len- mostra o comprimento da frase, que subtraído de -1,
# Dará a última posição.#
