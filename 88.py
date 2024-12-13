from random import randint
lista = []
operador = 0
palpite = int(input('Quantos jogos você quer: '))
for numero in range(0,palpite):
    lista_secundaria = []
    while operador < 6:
        sorte = randint(1,60)
        if sorte not in lista_secundaria:
            lista_secundaria.append(sorte)
            operador += 1
    operador -= 6
    lista_secundaria.sort()
    lista.append(lista_secundaria)
    print(f'JOGO {numero+1}:{lista[numero]}')
