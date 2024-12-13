continua = False
soma = 0
cont = 0
maior = 0
menor = 99999
while not continua:
    num = int(input('Digite um número inteiro qualquer: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    vi = input('Quer continuar? (S ou N) ').lower()
    if vi == 'n':
        continua = True
print(f'A média dos números digitos é {soma/cont:.2f}, o maior {maior}, o menor {menor}.')