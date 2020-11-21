#Faça um programa que leia uma temperatura em graus celsius e converta
#para fahrenheit.

celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celsius * 9/5) + 32
print('O valor convertido de {}ºC em fahrenheit é {}ºF'.format(celsius, fahrenheit))
