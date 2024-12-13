from datetime import date
def voto(idade):
    idade = atual_ano-ano
    if 65 > idade >= 18:
        return f'Com {idade} anos seu voto e obrigatorio.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos seu voto e opicional.'
    else:
        return f'Com {idade} anos você não pode votar.'


ano = int(input('Em que ano você nasceu? '))
atual_ano = date.today().year
print(voto(ano))
