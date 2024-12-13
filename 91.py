from random import randint
from time import sleep
print('PALPITES')
print('-'*30)
jogo = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6)}
ordem = sorted(jogo.values(), reverse=True)
nome = []
for chave, valor in jogo.items():
    sleep(1)
    print(f'Palpite {chave} com {valor}')
print('-'*30)
print('Em ordem a colocação fica:')
print('-'*30)
numero = 1
for e in ordem:
    sleep(1)
    for chave, valor in jogo.items():
        if e == valor and chave not in nome:
            print(f'{numero}º colocado: {chave} com {valor}')
            nome.append(chave)
            break
    numero += 1
