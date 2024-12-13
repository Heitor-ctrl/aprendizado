from random import randint
tupla = tuple(randint(0,9) for i in range(0,5))
print(f'Esses são os número sorteados {tupla}.')
print(f'O maior valor é {max(tupla)}.')
print(f'O menor valor é {min(tupla)}.')