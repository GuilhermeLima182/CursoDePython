# Desenvolva um programa que leia o compriemnto de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Digite o 1º comprimento: '))
r2 = float(input('Digite o 2º comprimento: '))
r3 = float(input('Digite o 3º comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 < + r2:
    print('Esses comprimentos formam um triângulo.')
else:
    print('Esses comprimentos não formam um triângulo')
