maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual e o peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f} Kg, o menor é {:.2f} Kg.'.format(maior, menor))