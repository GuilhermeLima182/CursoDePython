#Faça um programa que leia o comprimento do cateto oposto e do adjacente,
#de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
b = float(input('Qual o comprimento do cateto oposto? '))
c = float(input('Qual o comprimento do cateto adjacente? '))
a = hypot(b, c)
print('O comprimento da hipotenusa é {:.2f}'.format(a))
