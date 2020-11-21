# A confederação Nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria,de acordo
#com a idade:
# - até 9 anos: mirin
# - até 14 anos: infantil
# - até 19 anos: junior
# - até 20 anos: sênior
# - acima: master
from datetime import date
atual = date.today().year
anos = int(input('Qual o seu ano de nascimento? '))
idade = atual - anos
if idade <= 9:
    print(' Você tem {} anos e sua categoria é \033[0;30mMIRIN\033[m.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é \033[31mINFANTIL\033[m.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é \033[32mJUNIOR\033[m.'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é \033[33mSÊNIOR\033[m'.format(idade))
else:
    print('Você tem {} anos e sua categoria é \033[34mMASTER\033[m.'.format(idade))
