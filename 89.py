lista = []
media = []
while True:
    nome = input('Digite o nome: ').title().strip()
    lista_nome = []
    lista_nome.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    soma = (nota1 + nota2)/2
    media.append(soma)
    lista_nota = []
    lista_nota.append(nota1), lista_nota.append(nota2)
    lista_nome.append(lista_nota)
    lista.append(lista_nome)
    decisao = ' '
    while decisao not in 'SsNn':
        decisao = str(input('Quer continuar?[S/N] '))[0]
    if decisao in 'Ss':
        soma = 0
    if decisao in 'Nn':
        break
for posicao, item in enumerate(lista[:]):
        for valor, num in enumerate(item):
            print(valor)
        print()