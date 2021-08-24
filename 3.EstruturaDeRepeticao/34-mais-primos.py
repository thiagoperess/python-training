# Exercício 34

# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

count = 0
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[32m', end='')
        count += 1
    else:
        print('\033[33m', end='')
    print(f'{i}', end=' ')

print(f'\n\033[m{num} é divisível {count}x.')

if count == 2:
    print('É primo.')
else:
    print('Não é primo.')