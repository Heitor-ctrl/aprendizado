termo = int(input('Qual é o primeiro termo da PA: '))
razao = int(input('Qual é a razão da PA: '))
decimo = termo+(10-1)*razao
while termo <= decimo:
    print(termo, end=' ')
    termo+=razao
new = int(input('\nQuer ver mais termos da PA? (1 = Sim/ 0 = Não) '))
nf = False
while not nf:
    if new == 1:
        novo = int(input('\nQuantos termos você deseja ver? '))
        if novo == 0:
            nf = True
        num = termo+(novo-1)*razao
        while termo <= num:
            print(termo, end=' ')
            termo += razao
    elif new == 0:
        nf = True
print('Fim do Programa!')