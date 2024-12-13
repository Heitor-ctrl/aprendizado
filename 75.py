valor = (int(input('Digite um número: ')),
        int(input('Outro número: ')),
        int(input('Mais um número: ')),
        int(input('O último número: ')))
print(f'Você dogitou {valor}')
print(f'O número 9 aparece {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O número 3 aparece a primeira vez em {valor.index(3)+1}ª lugar.')
else:
    print('O número 3 não aparece.')
print(f'Os valores pares digitados foram', end=' ')
for v in valor:
    if v % 2 == 0:
        print(v, end=' ')