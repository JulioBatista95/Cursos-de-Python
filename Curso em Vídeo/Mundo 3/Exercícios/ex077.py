palavras = ('aprender', 'python', 'ansiedade', 'raiva', 'medo', 'desconforto',
            'solidão', 'desespero', 'tristeza', 'alegria', 'calma', 'esperança',
            'depressão', 'futuro', 'programar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')