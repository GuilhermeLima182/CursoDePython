#Nessa aula, vamos começar nossos estudos com os laços
# e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender.
# Por exemplo:

i = int(input('Início: '))
f = int(input('fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')