#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia o nome
#dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = str(input('Qual é o primeiro aluno? '))
nome2 = str(input('Qual é o segundo aluno? '))
nome3 = str(input('Qual é o terceiro aluno? '))
nome4 = str(input('Qual é o quarto aluno? '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de alunos é: ')
print(lista)

