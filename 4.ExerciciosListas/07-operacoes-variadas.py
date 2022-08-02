
# Exercício 07

# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
multiplicacao = 1

for i in range(5):
    numero = int(input(f'Digite o {i+1} número: '))
    numeros.append(numero)
    cont = numero
    multiplicacao *= cont

print(sum(numeros))
print(multiplicacao)
print(numeros)