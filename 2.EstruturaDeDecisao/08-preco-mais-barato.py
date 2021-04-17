# Exercício 08

# Faça um programa que pergunte o preço de três produtos e informe qual 
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

list1 = list()
for i in range(0, 3):
    produto = float(input(f'Qual o preço do produto R$ '))
    list1.append(produto)
print(f'O produto mais barato custa R$ {min(list1):.2f}')
