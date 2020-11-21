# Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.


v = float(input('Qual a velocidade atual do carro? '))
multa = (v - 80) * 7
if v > 80:
    print('Você foi multado! Terá que pagar R${:.2f}'.format(multa))
print('Você está na velocidade permitida')
