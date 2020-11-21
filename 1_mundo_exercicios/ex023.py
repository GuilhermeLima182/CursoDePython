#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input('Digite um número de 0 á 9999: ')
print('unidade: {}'.format(numero[3:4]))
print('dezena: {}'.format(numero[2:3]))
print('centena: {}'.format(numero[1:2]))
print('milhar: {}'.format(numero[0:1]))
