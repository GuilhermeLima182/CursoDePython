# escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# não existe valor maior, os dois são iguais

primeiroValor = int(input('Digite o primeiro valor: '))
segundoValor = int(input('Digite o segundo valor: '))

if primeiroValor > segundoValor:
    print('O primeiro valor é maior que o segundo valor')
elif segundoValor > primeiroValor:
    print('O segundo valor é maior que o primeiro valor')
else:
    print('Os dois valores são iguais')
