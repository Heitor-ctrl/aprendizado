dicionario = dict()
lista = list()
while True:
    dicionario['nome'] = str(input('Nome: ')).title()
    dicionario['media'] = float(input('Média: '))
    if dicionario['media'] > 6.9:
        dicionario['situacao'] = 'Aprovado'
    elif 5 <= dicionario['media'] < 7:
        dicionario['situacao'] = 'Recuperação'
    else:
        dicionario['situacao'] = 'Reprovado'
    lista.append(dicionario.copy())
    dec = ' '
    while dec not in 'SsNn':
        dec = str(input('Quer continuar?[S/N] ')).lower()[0]
    if dec == 'n':
        break
for ponto in lista:
    print(f'{ponto["nome"]} ficou com a média {ponto["media"]}, e sua situação é {ponto["situacao"]}.')
