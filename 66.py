print('Para sair do programa digite 999')
soma = cont = 0
while True:
    n = int(input('Digite um número inteiro qualquer: '))
    if n == 999:
        break
    soma+=n
    cont += 1
print(f'Você digitou {cont} números, e a soma entre eles é {soma}.')