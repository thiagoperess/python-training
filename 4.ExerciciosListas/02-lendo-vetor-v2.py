# Exercício 02

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = [
    float(input(
    f'Número {i+1}: ')) 
    for i in range(10)
          ]

print(numeros[::-1])
