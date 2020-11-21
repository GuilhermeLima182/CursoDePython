dist = float(input('Qual a distância da viagem em Km? '))
preco1 = (0.50 * dist)
preco2 = (0.45 * dist)
if dist <= 200:
    print('O valor da passagem é: R${:.2f}'.format(preco1))
else:
    print('O valor da passagem é: R${:.2f}'.format(preco2))
