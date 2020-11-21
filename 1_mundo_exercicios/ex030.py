# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print('número é par')
else:
    print('número é impar')
