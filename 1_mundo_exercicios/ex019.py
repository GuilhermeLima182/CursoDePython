#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido

import random
nome1 = str(input('Qual é o primeiro aluno? '))
nome2 = str(input('Qual é o segundo aluno? '))
nome3 = str(input('Qual é o terceiro aluno? '))
nome4 = str(input('Qual é o quarto aluno? '))
print('O aluno escolhido é {}'.format(random.choice([nome1, nome2, nome3, nome4])))
