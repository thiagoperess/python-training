# Exercício 32

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Digite um número: '))
count = num
fat = 1
print(f'Fatorial de {num}!')
while count > 0:
    print(f'{count}', end='')
    print(' . ' if count > 1 else ' = ', end='')
    fat *= count
    count -= 1
print(f'{fat}')