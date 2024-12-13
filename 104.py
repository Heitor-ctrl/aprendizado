def leiaint(inteiro):
    while True:
        inteiro = input('\033[97mDigite um número: ')
        inteiro2 = inteiro[0]
        if inteiro2 not in '0123456789':
            print('\033[91m ERRO! Digite um número inteiro válido.')
        elif inteiro2 in '0123456789':
            return inteiro
            break


inteiro = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {inteiro}.')
