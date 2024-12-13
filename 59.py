valor_1 = int(input('Digite um valor inteiro qualquer: '))
valor_2 = int(input('Digite outro valor inteiro qualquer: '))
print(('-=') * 15, 'MENU', ('-=') * 15)
print('''[1] - Somar
[2] - Multiplicar
[3] - maior
[4] - Novos números
[5] - Sair do programa''')
print(('-=')*33)
valor = False
while not valor:
    escolha = input('Qual é a sua escolha? ')
    if escolha == '1':
        print('{} + {} = {}'.format(valor_1, valor_2, valor_1+valor_2))
    if escolha == '2':
        print('{} x {} = {}'.format(valor_1, valor_2, valor_1*valor_2))
    if escolha == '3':
        valor_1
        valor_2
        if valor_1 > valor_2:
            print('O maior número é {}.'.format(valor_1))
        else:
            print('O maior número é {}'.format(valor_2))
    if escolha == '4':
        valor_1 = int(input('Novo número: '))
        valor_2 = int(input('Outro número: '))
    if escolha == '5':
        valor = True
print('Fim Do Programa!')