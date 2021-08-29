# Exercício 08

# Faça um programa que pergunte o preço de N produtos e informe qual 
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

lista = []

for i in range(3):
    produto = float(input(f'Preço do {i+1}º produto R$ '))
    lista.append(produto)

menor = lista[0]

if lista[0] > lista[1] < lista[2]:
    menor = lista[1]

elif lista[0] > lista[2] < lista[1]:
    menor = lista[2]

print(f'O produto mais barato custa R$ {menor:.2f}')
