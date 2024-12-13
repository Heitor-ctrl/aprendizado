numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze')
num = ('quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
tuplas = numeros + num
escolha = int(input('Qual número você quer ver entre 0 e 20? '))
while escolha > 20:
    escolha = int(input('Qual número você quer ver entre 0 e 20? '))
print(f'O número {escolha} por extenso é {tuplas[escolha]}.')
