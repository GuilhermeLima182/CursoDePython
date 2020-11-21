# Faça um programa que leia uma frase pelo teclado e mostre:
#* Quantas vezes aparece a letra "A"
#* em que posição ela aparece pela primeira vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas vezes aparece a letra A: {}'.format(frase.count('A')))
print('1º posição: {}'.format(frase.find('A')+1))
print('2] posição: {}'.format(frase.rfind('A')+1))