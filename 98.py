from time import sleep
def tamanho():
    print('Contagem de 1 em 1 de forma progressiva')
    for valor in range(1,11):
        print(valor, end=' ')
        sleep(0.5)
    print()
    print('Contagem de 2 em 2 de forma regressiva')
    for numero in range(10,-1,-2):
        print(numero, end=' ')
        sleep(0.5)
    print()
    num = int(input('Digite onde começar: '))
    num2 = int(input('Digite o ultimo numero: '))
    num3 = int(input('Quer pular quantos numero até lá: '))
    if num2 > num:
        if num3 < 0:
            num3 = num3 * -1
    if num3 == 0:
        num3 = -1
    for valor in range(num, num2+1, num3):
        print(valor, end=' ')
    print('FIM!')
tamanho()