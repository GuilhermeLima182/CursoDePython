#Faça um programa que mostre quanto a pessoa tem na carteira,
#e quanto ela pode comprar em dólares.
# cotação = USD$3.27

valorCarteira = float(input('Qual o valor em reais que você têm na carteira? R$ '))
dolares = valorCarteira / 3.27
print('Você pode comprar US${:.2f} dólares com o dinheiro que você têm'.format(dolares))
