import datetime
programa = dict()
programa['nome'] = input('Nome: ').title()
data_nascimento = int(input('Ano de nascimento: '))
hoje = datetime.date.today().year
idade = programa['idade'] = hoje - data_nascimento
carteira = programa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if carteira != 0:
    contrato = programa['ano de contratação'] = int(input('Em que ano foi contratado? '))
    programa['salario'] = float(input('Qual e o seu salário atual? '))
    calculo = 35-(hoje-contrato)+idade
    programa['aposentadoria'] = calculo
print('-'*30)
print('Seus dados:')
print('-'*30)
for chave, valor in programa.items():
    print(f'{chave} tem o valor {valor}.')
print('-'*30)
