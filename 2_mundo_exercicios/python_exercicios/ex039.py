# Faça um programa que leia o ano de nascimento de um
# jovem e informe,de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar.
# - se é a hora de se alistar.
# - se já passou do tempo do alistamento
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nasc = int(input("Qual é o ano do seu nascimento? "))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda não pode se alistar,falta {} anos para se alistar.'.format(saldo))
elif idade == 18:
    print('Você completou 18 anos e já pode se alistar.')
elif idade > 18:
    saldo = idade - 18
    print('já se passaram {} anos para vc se alistar'.format(saldo))
