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


def moeda(preco=0, moeda= 'R$', sit=False):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
