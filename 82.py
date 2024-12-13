lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    dec = ' '
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    while dec not in 'SN':
        dec = input('Quer continuar?[S/N] ').upper()[0]
    if dec == 'N':
        break
print(f'Sua lista é {lista}.')
print(f'Sua lista com números pares é {par}')
print(f'Sua lista com números ímpares é {impar}.')