# Exercício 23

# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

count = 0
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[32m', end='')
        count += 1
    else:
        print('\033[33m', end='')
    print(f'{i}', end=' ')
    
print(f'\n\033[mO número {num} foi disível {count} vezes.')

if count == 2:
    print('Portanto, este é um número primo.')
else:
    print('Logo, este não é um número primo.')