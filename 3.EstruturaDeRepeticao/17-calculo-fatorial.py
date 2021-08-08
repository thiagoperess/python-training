# Exercício 17

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# Solução 1 (com a lib math):

from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}')

# Solução 2:

num = int(input('Digite um número: '))
count = num
fat = 1
print(f'Calculando {num}!')
while count > 0:
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat *= count
    count -= 1
print(f'{fat}')