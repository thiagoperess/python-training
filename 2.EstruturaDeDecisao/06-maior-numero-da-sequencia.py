# Exercício 06

# Faça um Programa que leia três números e mostre o maior deles. 

list1 = list()
for i in range(0,3):
    num = int(input(f'Digite o {i+1}º número: '))
    list1.append(num)
print(list1)
print(f'O maior número é {max(list1)}.')