jogo = {}
lista = []
nome = jogo['nome'] = input('Nome: ').title()
partida = jogo['partida'] = int(input(f'Quantas partidas {nome} jogou? '))
soma = 0
for campo in range(partida):
    gols = int(input(f'Quantos gols na partida {campo}? '))
    lista.append(gols)
    jogo['gols'] = lista
    soma += gols
    jogo['total de gols'] = soma
print('-'*30)
print(jogo)
print('-'*30)
print(f'O jogador {nome} jogou 5 partidas.')
for posicao, valor in enumerate(lista):
    print(f'=> Na partida {posicao}, fez {valor} gols.')
print(f'No total foram {soma} gols na temporada.')