def leiaint(inteiro):
    while True:
        try:
            inteiro = int(input('\033[97mDigite um número inteiro: '))
        except ValueError:
            print('\033[91mErro: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[91mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return inteiro


def leiafloat(real):
    while True:
        try:
            real = float(input('\033[97mDigite um número real: ').replace(',', '.'))
        except ValueError:
            print('\033[91mErro: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[91mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return real


valor_inteiro = leiaint(inteiro=True)
valor_real = leiafloat(real=True)
print(f'O valor inteiro digitado foi {valor_inteiro} e o real foi de {valor_real}')
