from random import randint
from time import sleep
def leitor(secundaria):
    return len(secundaria)
def selecao(numero):
    if numero not in secundaria:
        secundaria.append(numero)
def maior(secundaria):
    if secundaria:
        print(f'O maior valor passado é {max(secundaria)}.')
    else:
        print('Nenhum valor foi passado.')
secundaria = []
print('-'*45)
print('Analisando os valores passados...')
for valor in range(randint(1,7)):
    numero = randint(0, 10)
    print(numero, end=' ')
    sleep(0.5)
    selecao(numero)
print(f'Foram informados {leitor(secundaria)} valores ao todo.')
maior(secundaria)
secundaria.clear()
print('-'*45)
print('Analisando os valores passados...')
for valor in range(randint(1, 7)):
    numero = randint(0,10)
    print(numero, end=' ')
    sleep(0.5)
    selecao(numero)
print(f'Foram informados {leitor(secundaria)} valores ao todo.')
maior(secundaria)
secundaria.clear()
print('-'*45)
for valor in range(randint(1, 7)):
    numero = randint(0, 10)
    print(numero, end=' ')
    sleep(0.5)
    selecao(numero)
print(f'Foram informados {leitor(secundaria)} valores ao todo.')
maior(secundaria)
