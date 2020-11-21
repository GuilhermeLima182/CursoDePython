# Escreva um programa que pergunte o salário de um funcionário e calculae o valor do seu aumento.
#para salários superiores a R$ 1.250,00,calcule um aumento de 10%
#para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Quanto é o seu salário? '))
aumento1 = salario * 1.10
aumento2 = salario * 1.15
if salario <= 1.250:
    print('Seu salário com o aumento é de: {:.2f}'.format(aumento1))
else:
    print('Seu novo salário é de: {:.2f}'.format(aumento2))
