from random import randint
print('Vamos jogar, vou pensar em um número entre 0 e 5.')
sorte = randint(0, 5)
jogador = input('Em que número eu pensei? ')
while jogador != sorte:
    jogador = int(input('Você errou tente de novo: '))
print('Você acertou!')
# Resolução Guanabara
from random import randint
computador = randint(0, 10)
print('Tente acertar o número em que pensei entre 0 e 10')
acertou = False
palpite = 0
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    palpite += 1
    if player == computador:
        acertou = True
    else:
        if player < computador:
            print('Mais... Tente mais uma vez.')
        elif player > computador:
            print('Menos... Tente mais uma vez.')
print('Você acertou, precisou de {} tentativas, Parabéns!'.format(palpite))