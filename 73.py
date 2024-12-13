classificacao = ('Flamengo', 'Palmeiras', 'Botafogo', 'Athletico-PR', 'Bahia',
                     'Internacional', 'Cruzeiro', 'São Paulo', 'Bragantino', 'Atletico-MG',
                     'Juventude', 'Fortaleza', 'Criciúma', 'Cuiabá', 'Vasco da Gama', 'FC Vitória',
                     'Atletico-GO', 'Corinthians', 'Grêmio', 'Fluminense')
print(classificacao)
print(f'Os times {classificacao[0:5]}, são os primeiros colocados.')
print(f'Os times {classificacao[-4:]}, são os últimos colocados.')
print(f'Em ordem alfabética é {sorted(classificacao)}')
print(f'O cruzeiro está na posição {classificacao.index('Cruzeiro')+1}')