# Exercício 27

# Faça um Programa que leia N números e mostre-os em ordem decrescente. 

lista = []
qty_num = int(input('Quantos números? '))

for i in range(qty_num):
    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)

print(sorted(lista, reverse=True))