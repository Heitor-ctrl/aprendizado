matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = []
valor = soma = 0
for linha in range(3):
    for coluna in range(3):
        num = matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if num % 2 == 0:
            par.append(num)
            soma += num
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {soma}')
soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
for linha in range(3):
    for coluna in range(1):
        valor += matriz[linha][2]
print(valor)
