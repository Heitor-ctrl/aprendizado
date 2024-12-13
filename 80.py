numero = list()
for n in range(0, 5):
    valor = int(input('Digite um valor: '))
    for chave, num in enumerate(numero):
        if valor < num:
            numero.insert(chave, valor)
            break
    else:
        numero.append(valor)
print(numero)

                        #GUANABRA
lista = []
for d in range(5):
    digito = int(input('Digite um valor: '))
    if d == 0 or digito >= lista[-1]:
        lista.append(digito)
    else:
        pos = 0
        while pos < len(lista):
            if digito < lista[pos]:
                lista.insert(pos, digito)
                break
            pos += 1
print(lista)