soma = 0
maior = 0
count = 0
nom = ''
for c in range(1,5):
    print('{} PESSOA'.format(c))
    nome = input('Qual o nome da pessoa: ').title()
    idade = int(input('Quantos anos ela tem: '))
    sexo = input('Qual o sexo da pessoa use M (masculino) e F (feminino): ').upper()
    soma += idade
    if c == 1:
        maior = idade
        nom = nome
    if sexo == 'M':
        maior = idade
        nom = nome
    if sexo == 'F' and idade < 20:
        count += 1
print('A média de idade do grupo é {} anos.'.format(soma/c))
print('O homem mais velho tem {} anos, seu nome é {}.'.format(maior, nom))
print('{} mulheres são abaixo de 20 anos.'.format(count))