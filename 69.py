masc = menor = maior = 0
while True:
    idade = int(input('Qual é a sua idade? '))
    sexo = input('Qual é o seu sexo? ').strip().upper()[0]
    continua = input('Quer continuar? S/N ').upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    if continua == 'N':
        break
print(f'{maior} pessoas são acima de 18 anos.')
print(f'Foram cadastrado {masc} homens.')
print(f'{menor} mulheres são abaixo de 20 anos.')