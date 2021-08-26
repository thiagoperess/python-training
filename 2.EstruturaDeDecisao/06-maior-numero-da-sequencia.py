# Exercício 06

# Faça um programa que leia três números e mostre o maior deles.
# OBS: Não utilize a funções 'min' e 'max'.

lista = []
for i in range(3):
    num = int(input(f'{i+1}º número: '))
    lista.append(num)

maior = lista[0]

if lista[0] < lista[1] > lista[2]:
    maior = lista[1]

elif lista[0] < lista[2] > lista[1]:
    maior = lista[2]

print(f'O maior valor digitado foi {maior}')