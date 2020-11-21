#Faça um programa que mostra os tipos primitivos do valor digitado

a = input('Digite algo: ')
print('o tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético', a.isalpha())
print('Está em maiúscula?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está captalizada?', a.capitalize())

