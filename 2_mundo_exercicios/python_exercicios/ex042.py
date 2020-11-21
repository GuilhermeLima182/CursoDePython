# Refaça o exercicio 35 dos triângulos,acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-=-' * 10)
print('analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Digite o 1º comprimento: '))
r2 = float(input('Digite o 2º comprimento: '))
r3 = float(input('Digite o 3º comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 < + r2:
    print('Esses comprimentos formam um triângulo.')
elif r1 == r2 == r3:
    print('Esse triângulo possui todos os lados iguais,por isso é um triângulo \033[33mequilátero\033[m')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Esse triângulo possui dois lados iguais ,por isso é um triângulo \033[34misósceles\033[m')
elif r1 != r2 or r2 != r3 or r3 != r1:
    print('Esse triângulo possui todos os lados diferentes,por isso é um triângulo \033[35mescaleno\033[m')
else:
    print('Esses comprimentos não formam um triângulo')
