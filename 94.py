principal = list()
maior = []
mulheres = list()
informacoes = dict()
soma = 0
while True:
    nome = informacoes['nome'] = input('Nome: ').title()
    sexo = informacoes['sexo'] = input('Sexo: ').upper()[0]
    idade = informacoes['idade'] =int(input('Idade: '))
    soma += idade
    principal.append(informacoes.copy())
    if sexo == 'F':
        mulheres.append(nome)
    dec = ' '
    while dec not in 'SsNn':
        dec = input('Quer continuar? ').upper()
    if dec == 'N':
        break
media = soma/len(principal)
print('-'*60)
print(f'No total foram cadastradas {len(principal)}.')
print(f'A média de idade do grupo foi de {media:.2f}.')
if len(mulheres) > 0:
    print(f'Ao todo foram cadastradas {len(mulheres)}, {mulheres}.')
else:
    print('Não houve cadastro de mulheres.')
for posicao in principal:
    if posicao["idade"] > media:
        maior.append(posicao["nome"])
print(f'As pessoas com idade maior que a média é {maior}.')
