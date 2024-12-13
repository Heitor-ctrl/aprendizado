palavra = ('cruzeiro', 'computador', 'moto', 'apartamento', 'fone')
for p in palavra:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')