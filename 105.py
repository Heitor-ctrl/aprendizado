def notas(*num: float, sit=False):
    """
    Mostra um dicionário com a quantidade de notas dos alunos, a maior e a menor nota com a média e a situação.
    :param num: Notas dos alunos.
    :param sit: Passa a situação dos alunos.
    """
    lista = []
    for numero in num:
        lista.append(numero)
    quantidade = len(lista)
    soma = sum(lista)/quantidade
    boletim = {}
    maior = menor = 0
    for posicao, numero in enumerate(lista):
        if posicao == 0:
            maior = numero
            menor = numero
        if maior < numero:
            maior = numero
        if menor > numero:
            menor = numero
    boletim['total'] = quantidade
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = soma
    if sit:
        if soma >= 7:
            boletim['situação'] = 'BOA'
        elif 5 <= soma < 7:
            boletim['situação'] = 'REGULAR'
        else:
            boletim['situação'] = 'RUIM'
    print(boletim)

notas(8, 7, 9, 4, 6, 8, sit=True)
