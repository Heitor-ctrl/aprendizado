from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0,10)
    opcao = input('PAR OU ÍMPAR? ').strip().lower()
    resp = jogador + pc
    print(f'Você escolheu {jogador}, e o computador {pc}, o resultado foi {resp}')
    if opcao == 'par' and resp % 2 == 0:
        print('Você ganhou!')
    if opcao == 'impar' and resp % 2 > 0:
        print('Você ganhou!')
    if opcao != 'par' and 'impar':
        print('Opção inválida, tente de novo!')
    else:
        print('Você perdeu!')
        break