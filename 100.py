from random import randint
from time import sleep
numeros = list()
def sorteia():
    return randint(1,9)


def somapar():
    pares = 0
    for valor in numeros:
        if valor % 2 == 0:
            pares += valor
    print(pares)


print('Analisando a lista criada')
for valor in range(5):
    chave = sorteia()
    numeros.append(chave)
print(f'Sua lista é {numeros}')
print('A soma dos números pares são', end=' ')
somapar()
