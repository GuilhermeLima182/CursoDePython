#Faça um programa que leia quantos dias o carro foi alugado,e quantos
#kilômetros foram percorridos,e mostre o valor total a pagar.
#sabendo que 1 dia = R$60,00 + 0,15 centavos por km rodado.

km = float(input('Quantos kilômetros foram percorridos?'))
dias = float(input('Quantos dias alugados? '))
preco = (60 * dias) + (0.15 * km)
print('O preço a pagar é {}'.format(preco))
