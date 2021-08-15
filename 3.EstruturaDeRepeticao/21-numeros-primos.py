# Exercício 20

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

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