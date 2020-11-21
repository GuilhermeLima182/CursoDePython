#Crie um programa que leia o nome completo de uma pessoa e mostre:
#* o nome com todas as letras minúsculas
#* o nome com todas as letras maiúsculas
#* quantas letras ao todo(sem considerar espaços)
#* Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo? ')).strip()
print('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele têm {} letras'.format(separa[0], len(separa[0])))
