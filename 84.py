pessoas = []
tudo = []
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')).title())
    pessoas.append(float(input('Peso: ')))
    tudo.append(pessoas[:])
    pessoas.clear()
    cont = ' '
    while cont not in 'SsNn':
        cont = input('Quer continuar?[S/N] ')[0]
    if cont in 'Nn':
        break
print(f'{len(tudo)} pessoas foram cadastradas.')
for p in tudo:
    pessoas.append(p[1])
for posicao, valor in enumerate(pessoas):
    if posicao == 0:
        mai = valor
    if mai < valor:
        mai = valor
for posicao, valor in enumerate(pessoas):
    if posicao == 0:
        men = valor
    if men > valor:
        men = valor
for posicao, valor in enumerate(tudo):
    if mai in valor:
        print(f'O maior peso é {mai} Kg, e a pessoa se chama {posicao}.')
    if men in valor:
        print(f'O menor peso é {men} Kg, e a pessoa se chama {posicao}.')
