# Exercício 18

# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

list1 = []
len_list1 = int(input('Tamanho da lista: '))

for i in range(len_list1):
    nums = int(input(f'Digite o {i+1}º número: '))
    list1.append(nums)

print(f'O maior número é {max(list1)}' )
print(f'O menor número é {min(list1)}')
