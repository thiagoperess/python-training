# Exercício 09

# Faça um Programa que leia três números e mostre-os em ordem decrescente. 

list1 = list()
for i in range(0, 3):
    num = int(input('Digite um número: '))
    list1.append(num)
print(sorted(list1, reverse=True))