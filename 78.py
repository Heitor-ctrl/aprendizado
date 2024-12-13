valor = list()
maior = menor = 0
for c in range(5):
    n = int(input(f'Digite o {c} valor: '))
    valor.append(n)
    if c == 0:
        maior = valor[c]
        menor = valor[c]
    if maior < valor[c]:
        maior = valor[c]
    if menor > valor[c]:
        menor = valor[c]
print(f'Os valores que você digitou é {valor}.')
print(f'O maior valor é {maior}, e sua posição é ', end='')
for v, n in enumerate(valor):
    if n == maior:
        print(v,'...', end='')
print()
print(f'O menor valor é {menor}, e sua posição é ', end='')
for v, n in enumerate(valor):
    if n == menor:
        print(v,'...',end='')