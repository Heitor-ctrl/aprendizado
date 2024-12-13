def contador(texto):
    tanto = len(texto)+4
    print('~'*tanto)
    print(f'  {texto}')
    print('~'*tanto)

digita = input('Digite um texto qualquer: ')
contador(digita)