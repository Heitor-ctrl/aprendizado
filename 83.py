mat = str(input('digite a expressão: '))
lista = []
for sim in mat:
    if sim == '(':
        lista.append('(')
    elif sim == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append('(')
            break
if len(lista) == 0:
    print('Tentativa válida!')
else:
    print('Tentativa inválida!')