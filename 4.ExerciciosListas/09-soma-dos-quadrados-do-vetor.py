# Exercício 09

# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

vetorA = []

for i in range(3):
    num = int(input(f'Digite o {i+1}º número: '))
    num *= num
    vetorA.append(num)

print(vetorA)