# Exercício 23

# Faça um programa que mostre todos os números entre 1 e N 
# sendo N um número inteiro fornecido pelo usuário. Destaque os números 
# divisíveis com caracteres ANSI, e responda se ele é primo ou não. 

# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

count = 0
divide = []
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[32m', end='')
        count += 1
        divide.append(i)
        
    else:
        print('\033[33m', end='')
    print(f'{i}', end=' ')
    
print(f'\n\033[mO número {num} foi disível {count} vezes.')    
print(f'{num} é primo.' if len(divide) == 2 else f'{num} não é primo.')
