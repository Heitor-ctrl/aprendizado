valor = int(input('Quanto você quer sacar? R$'))
cont = cont1 = cont2 = cont3 = 0
while valor >= 50:
    valor -= 50
    cont += 1
while valor >= 20:
    valor -= 20
    cont1 += 1
while valor >=10:
    valor -= 10
    cont2 += 1
while valor > 0:
    valor -= 1
    cont3 += 1
print(f'Total de {cont} cédulas de R$50.')
print(f'Total de {cont1} cédulas de R$20.')
print(f'Total de {cont2} cédulas de R$10.')
print(f'Total de {cont3} cédulas de R$1.')