print('Cálculadora de fatorial')
num = int(input('Qual número você quer saber? '))
for n in range(num, 1, -1):
    n -= 1
    a = n
    print('{} x {} ='.format(num, n), end=' ')
    num *= n
print(num)
# Usando WHILE
c = int(input('Qual número você quer saber seu fatorial? '))
a = c
c -= 1
while c >= 1:
    print(f"{a}x{c} =", a * c, end=' ')
    a *= c
    c -= 1
