lista = [{'Nome': 'Ana Paula', 'Idade': 32}, {'Nome': 'Cláudio Mendonça', 'Idade': 18}, {'Nome': 'Gustavo Guanabara', 'Idade': 41},
         {'Nome': 'Maria Clara Peixoto', 'Idade': 65}, {'Nome': 'Maurício Souza', 'Idade': 19}, {'Nome': 'Pedro Gonçalves', 'Idade': 18},
         {'Nome': 'Nilce Pedrosa', 'Idade': 43}]

while True:
    print('-' * 40)
    print(' ' * 13, 'MENU PRINCIPAL')
    print('-' * 40)
    print('\033[94m1 - Ver pessoas cadastradas\033[0m \n'
          '\033[94m2 - Cadastrar nova pessoa\033[0m \n'
          '\033[94m3 - Sair do sistema\033[0m')
    print('-'*40)
    dec = int(input('Sua Opção: '))
    if dec == 3:
        print('-'*40)
        print('FIM DO PROGRAMA, ATÉ LOGO!')
        print('-'*40)
        break
    elif dec == 1:
        for item in lista:
            print(item['Nome'], item['Idade'], 'anos')
    elif dec == 2:
        dicionionario = dict()
        dicionionario['Nome'] = str(input('Nome: '))
        dicionionario['Idade'] = int(input('Idade: '))
        lista.append(dicionionario)
    else:
        print('\033[91mErro: Por favor, digite um número válido.\033[0m')