lista = [[], []]
for posicao in range(0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
        lista[0].sort()
    else:
        lista[-1].append(numero)
        lista[-1].sort()
print(f'Sua lista de números pares é {lista[0]}.')
print(f'Sua lista de números impares é {lista[-1]}.')
