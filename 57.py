input('Qual é o seu nome: ')
input('Qual é a sua idade: ')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual e o seu sexo (M ou F): ').upper()
'"Resolução Guanabara"'
sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sex))