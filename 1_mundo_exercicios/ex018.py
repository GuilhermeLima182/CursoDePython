#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno,cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = int(input('Digite um ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno do ângulo {} é {:.2f}'.format(angulo, sen))
print('O Cosseno do ângulo {} é {:.2f}'.format(angulo, cos))
print('A tangente do ângulo {} é {:.2f}'.format(angulo, tan))
