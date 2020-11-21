# Desenvolva uam lógica que leia o peso e a altura de uma pessoa
#calcule seu imc e mostre seu status,de acordo com a tabela abaixo:

# - abaixo de 18.5: abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida

peso = float(input('Digite aqui o seu peso em Kg: '))
altura = float(input('Digite aqui a sua altura em M: '))
imc = peso/(altura ** altura)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 >= imc < 30:
    print('Você está acima do seu peso')
elif 30 < imc < 40:
    print('Você está na obesidade.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')
