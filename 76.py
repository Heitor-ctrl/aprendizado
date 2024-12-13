unica = ('Lápis', 2, 'Caderno', 20, 'Mochila', 400, 'Tênis', 400, 'Blusa', 100)
for u in unica[0:-1:2]:
    print(f'{u}.................. R$ {unica[unica.index(u)+1]}')
