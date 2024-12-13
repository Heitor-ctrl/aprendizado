valor = list()
for v in range(0, 5):
    valor.append(input('Digite um número: '))
print(f'o maior valor que você digitou foi {max(valor)}, e está na posição {valor.index(max(valor))+1}')
print(f'O menor valor que você digitou foi {min(valor)}, e está na posição {valor.index(min(valor))+1}.')