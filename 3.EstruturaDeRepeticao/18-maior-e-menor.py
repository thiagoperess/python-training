# Exercício 18

# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

lista = []
qty_num = int(input('Quantidade de números: '))

for i in range(qty_num):
    nums = int(input(f'Digite o {i+1}º número: '))
    lista.append(nums)

print(f'''

O maior número é {max(lista)}
O menor número é {min(lista)}
E sua soma total é {sum(lista)}

''')
