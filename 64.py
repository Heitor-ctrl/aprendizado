print('Para sair do programa digite 999')
cont = 0
soma = num = 0
while num != 999:
    num = int(input('Digite um número inteiro qualquer: '))
    cont += 1
    soma += num
print(f'Você digitou {cont-1}, e a soma entre eles foi {soma-999}.')
print('Fim do programa!')