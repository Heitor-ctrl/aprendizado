from ex110 import moeda
def aumentar(preco, taxa, sit=False):
    res = preco+(preco*taxa/100)
    if sit:
        return moeda(res)
    else:
        return res


def diminuir(preco, taxa, sit=False):
    res = preco-(preco*taxa/100)
    if sit:
        return moeda(res)
    else:
        return res


def dobro(preco, sit=False):
    res = preco*2
    if sit:
        return moeda(res)
    else:
        return res


def metade(preco, sit=False):
    res = preco/2
    if sit:
        return moeda(res)
    else:
        return res


def moeda(preco=0, moeda= 'R$', sit=True):
    return f'{moeda} {preco:.2f}'.replace('.', ',')


def resumo(valor, maior=10, menor=5):
    print('-'*30)
    print(f' '*7, 'RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{maior}% de aumento: \t{aumentar(valor, maior, True)}')
    print(f'{menor}% de redução: \t{diminuir(valor, menor, True)}')
    print('-'*30)


def copia(valor=0):
    moeda.resumo(valor)
