#Faça um programa que pergunte ao usuario o valor do produto,
#e mostre o valor final com 5% de desconto.

valorProduto = float(input('Qual o valor do produto? R$ '))
desconto = (valorProduto * 5) / 100
vFinal = valorProduto - desconto
print('O valor do produto é R${}'.format(valorProduto))
print('O novo valor com  o desconto é de R${}'.format(vFinal))
