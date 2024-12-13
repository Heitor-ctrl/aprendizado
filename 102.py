def factorial(num=1, show=False):
    """
    ->Calcula o factorial de um número.
    :param num: O número a ser calculado.
    :param show: Show e a opção de mostrar ou não a operação.
    """
    calculo = 1
    for numero in range(num,0,-1):
        calculo *= numero
    if show:
        while True:
            print(f'{num} x', end=' ')
            num -= 1
            if num == 1:
                print(f'1 = {calculo}')
                break
    else:
        print(f'5! = {calculo}')


print('-'*30)
factorial(5, show=True)
help(factorial)
