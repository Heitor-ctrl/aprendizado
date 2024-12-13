zero = [[], [], []]
um = [[], [], []]
dois = [[], [], []]
for contador in range(3):
    valor = int(input(f'Digite um valor para [0,{contador}]: '))
    zero[contador].append(valor)
for contador in range(3):
    valor = int(input(f'Digite um valor para [1,{contador}]: '))
    um[contador].append(valor)
for contador in range(3):
    valor = int(input(f'Digite um valor para [2,{contador}]: '))
    dois[contador].append(valor)
print('-='*30)
print(f'{zero[0]} {zero[1]} {zero[2]}\n'
      f'{um[0]} {um[1]} {um[2]}\n'
      f'{dois[0]} {dois[1]} {dois[2]}')
# GUANABARA
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()