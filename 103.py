def ficha(nome='desconhecido', gols=0):
    if nome.strip() == '':
        nome = 'desconhecido'
    if gols.strip() == '' or not gols.isdigit():
        gols = int(0)
    else:
        gols = int(gols)
    print(f'O jogador {nome} fez {gols} na temporada.')


nome = str(input('Nome do jogador: '))
gols = input('Quantos gol marcou na temporada: ')
ficha(nome, gols)
