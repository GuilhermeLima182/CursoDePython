# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo_list = ['m', 'f']
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while sexo != m or f:
    str(input('Dados inválidos. Por favor, informe seu sexo: '))
if sexo == m or sexo == f:
    print('Sexo {} registrado com sucesso.'.format(sexo))
