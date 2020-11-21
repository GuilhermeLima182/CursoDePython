# Crie um programa que faça o computador jogar jokenpô com você.
import random
from time import sleep

print('=-=-='*10)
print('\033[0;34mBEM VINDO AO JOGO DE JOKENPÔ\033[m.')
print('=-=-='*10)
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = str(input('Escolha entre PEDRA,PAPEL E TESOURA e digite aqui sua escolha: ')).upper().strip()
print('Agora é a vez do computador.')
for contagem in range(0, 1):
    sleep(3)
print('Processando...')
for contagem in range(0, 1):
    sleep(5)
pc = random.choice(jogo)
print(pc)
if jogador == 'PAPEL' and pc == 'PAPEL':
    print('O jogo deu empate!')
elif jogador == 'PEDRA' and pc == 'PEDRA':
    print('O jogo deu empate!')
elif jogador == 'TESOURA' and pc == 'TESOURA':
    print('O jogo deu empate!')
elif jogador == 'PEDRA' and pc == 'PAPEL':
    print('O computador escolheu \033[34m{}\033[m,por isso você perdeu.'.format(pc))
elif jogador == 'PEDRA' and pc == 'TESOURA':
    print('O computador escolheu \033[34m{}\033[m,por isso você ganhou.'.format(pc))
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('O computador escolheu \033[34m{}\033[m,por isso você ganhou.'.format(pc))
elif jogador == 'PAPEL' and pc == 'TESOURA':
    print('O computador escolheu \033[34m{}\033[m,por isso você perdeu.'.format(pc))
elif jogador == 'TESOURA' and pc == 'PEDRA':
    print('O computador escolheu \033[34m{}\033[m,por isso você perdeu.'.format(pc))
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('O computador escolheu \033[34m{}\033[m,por isso você ganhou.'.format(pc))
