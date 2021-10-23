# Exercício 42

# Faça um programa que leia uma quantidade indeterminada de números positivos 
# e conte quantos deles estão nos seguintes intervalos: 

# [0-25], [26-50], [51-75] e [76-100]. 

# A entrada de dados deverá terminar quando for lido um número negativo.

n, c1, c2, c3, c4 = 1, 0, 0, 0, 0

while n >= 0:
    n = int(input('Digite um número: '))

    if 0 >= n <= 25:
        c1 += 1
    elif 26 >= n <= 50:
        c2 += 1
    elif 51 >= n <= 75:
        c3 += 1
    elif 76 >= n <= 100:
        c4 += 1

print(
      f'Números entre 0-25: {c1},\n'
      f'Números entre 26-50: {c2},\n'
      f'Números entre 51-75: {c3},\n' 
      f'Números entre 76-100: {c4},\n'
      )