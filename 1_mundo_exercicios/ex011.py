#Faça um programa que pergunte a altura e largura de uma parede,
# e a quantidade de tinta gasta para pintar essa parede sabendo que
# 1 L de tinta pinta 2m² da parede.

altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
area = largura * altura
tinta = area / 2
print('A quantidade de tinta necessária para pintar {}m² de parede vai ser de {} L'.format(area, tinta))
