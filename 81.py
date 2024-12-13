lista = []
num = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    num+=1
    while dec not in 'SN':
        dec = input('Quer continuar? [S/N] ').upper()[0]
        if dec == 'S':
            break
    if dec == 'N':
        break
    elif 5 in lista:
        a = lista.index(5)+1
print(f'Com base nas informações você digitou, essa lista tem {num} números.')
print('Sua lista em ordem decrescente,', sorted(lista, reverse=True))
if 5 in lista:
    print(f'O número 5 encontra-se na posição {a}.')
else:
    print('O número 5 não aparece na lista.')
