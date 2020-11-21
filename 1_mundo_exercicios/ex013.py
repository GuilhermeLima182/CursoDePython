#Faça um programa que leia um salário em reais, e depois mostre
# o novo salario com 15% de aumento.

salario = float(input('Qual é o seu salário em reais: R$ '))
salarioFinal = salario * 1.15
print('Seu novo salário é de R$ {:.2f}'.format(salarioFinal))
