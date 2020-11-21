#Faça um programa que mostre o dobro, o triplo e a raiz quadrada de um número

n = int(input('Digite um número: '))
print('O dobro de {} é {}.\n o triplo é {}\n e a sua raiz quadrada é {:.2f}'.format(n, (n * 2), (n * 3), (n ** (1/2))))
