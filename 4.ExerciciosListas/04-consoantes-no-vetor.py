# Exercício 04

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

vetor = []

for i in range(10):
    letras = str(input(f'Digite a {i+1}ª letra: '))
    if letras not in 'AaEeIiOoUu':
        vetor.append(letras)

print(vetor)