jogadores = []
jogo = {}
lista = []
while True:
    nome = jogo['nome'] = input('Nome: ').title()
    partida = jogo['partida'] = int(input(f'Quantas partidas {nome} jogou? '))
    soma = 0
    for campo in range(partida):
        gols = int(input(f'Quantos gols na partida {campo}? '))
        lista.append(gols)
        jogo['gols'] = lista[:]
        soma += gols
        jogo['total de gols'] = soma
    jogadores.append(jogo.copy())
    jogo.clear(), lista.clear()
    dec = ' '
    while dec not in 'SsNn':
        dec = input('Quer continuar?[S/N] ').upper()[0]
    if dec == 'N':
        break
print('-'*30)
for valor, posicao in enumerate(jogadores):
    print(f'Registro {valor} temos {posicao["nome"]} com {posicao["gols"]} gols nas partidas, e um total de {posicao["total de gols"]} gols na temporada.')
while True:
    cis = int(input('Qual o registro do jogador que você quer saber os dados? '))
    if cis == 999:
        print('Fim do programa!')
        break
    for valor, posicao in enumerate(jogadores):
        if cis == valor:
            print(f'Os dados do jogador são registro {valor}, nome {posicao["nome"]}, gols {posicao["gols"]}, total de gols {posicao["total de gols"]}.')
