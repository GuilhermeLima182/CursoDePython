#Faça um programa que converta um valor em metros para cm e mm

valorM = float(input('Digite o valor em metros: '))
valorC = valorM * 100
valorm = valorM * 1000
print('O valor convertido de {:.0f}M em centímetros é {:.0f}cm, e em milímetros é {} mm'.format(valorM, valorC, valorm))
