# Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem
#no final,de acordo com a média atingida:
# - média abaixo de 5.0: Reprovado
# - média entre 5.0 e 6.9: recuperação
# - média 7.0 ou superior: aprovado

nota01 = float(input('Digite a 1ª nota do aluno: '))
nota02 = float(input('Digite a 2ª nota do aluno: '))
media = (nota01 + nota02) / 2
if media < 5.0:
    print('sua nota é de {} pontos e está abaixo da média,por isso você está \033[0;31mREPROVADO\033[m'.format(media))
elif 5.0 <= media <= 6.9:
    print('Sua nota é de {} pontos,por isso você está de \033[0;33mRECUPERAÇÃO\033[m'.format(media))
elif media > 7.0:
    print('Sua nota é de {} pontos, por isso você foi \033[0;32mAPROVADO\033[m'.format(media))
