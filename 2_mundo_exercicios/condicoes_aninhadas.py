# Condições aninhadas

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Guilherme':
    print('Seu nome é bem popular no brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('\033[;34m Tenha um bom dia\033[m, \033[2;37m{}'.format(nome))
