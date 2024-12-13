total = contador = 0
barato = 99999
while True:
    nome = input('Qual é o produto que você deseja? ')
    preco = float(input('Qual é o preço do produto? R$'))
    mais = input('Quer continuar a comprar? S ou N ').upper().strip()[0]
    total += preco
    if preco > 1000.00:
        contador += 1
    if barato > preco:
        barato = preco
        if barato < preco:
            barato = preco
    if mais == 'N':
        break
print(f'O total da sua compra e R${total}.')
print(f'{contador} produtos custam mais de R$1000.00')
print(f'O seu produto mais barato custa R${barato}')