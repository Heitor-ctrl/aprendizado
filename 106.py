print('\033[0;30;44m~'*24)
print('\033[0;30;44m SISTEMA DE AJUDA PyHELP')
print('\033[0;30;44m~'*24)
print('\033[0;30;44mDigite fim para parar.\033[0;30;44m')
def manual(variavel):
    from time import sleep
    while True:
        variavel = input('\033[0;30;0mFunção ou Biblioteca > ').lower()
        if variavel == 'fim':
            break
        print('\033[0;30;41m~'*30)
        print(f"Acessando o manual do comando '{variavel}'")
        print('\033[0;30;41m~' * 30)
        sleep(1)
        print('\033[0;30;42m', end='')
        help(variavel)


manual(variavel=True)
