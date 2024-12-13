termo = int(input('Qual é o primeiro termo da PA: '))
razao = int(input('Qual é a razão da PA: '))
decimo = termo+(10-1)*razao
while termo <= decimo:
    print(termo, end=' ')
    termo += razao
