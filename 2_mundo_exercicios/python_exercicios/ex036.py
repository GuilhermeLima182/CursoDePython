# Escreva um programa para aprovar o empréstimo bancário
# para compra de uma casa. o programa vai perguntar o valor da casa
#,o salário do comprador e em quantos ele vai pagar.
# Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado

valorCasa = float(input('Qual é o valor total da casa? R$ '))
anos = int(input('Em quantos anos você deseja pagar? '))
salario = float(input('Qual é o seu salário total? R$ '))
parcela = valorCasa / (anos * 12)
aprovado = 0.3 * salario
print('O valor total da parcela é de R${:.3f}!'.format(parcela))
if parcela <= aprovado:
    print('Seu empréstimo está aprovado')
else:
    print('Seu empréstimo não foi aprovado')
