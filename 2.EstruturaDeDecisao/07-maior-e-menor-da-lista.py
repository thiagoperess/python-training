# Exercício 07

# Faça um Programa que leia três números e mostre o maior e o menor deles.

lista = []
for i in range(0,3):
    num = int(input(f'{i+1}º número: '))
    lista.append(num)

# verifica o MENOR

menor = lista[0]

if lista[0] > lista[1] < lista[2]:
    menor = lista[1]

elif lista[0] > lista[2] < lista[1]:
    menor = lista[2]

# verifica o MAIOR

maior = lista[0]

if lista[0] < lista[1] > lista[2]:
    maior = lista[1]

elif lista[0] < lista[2] > lista[1]:
    maior = lista[2]

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')