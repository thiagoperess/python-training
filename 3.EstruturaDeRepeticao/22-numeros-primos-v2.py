# Exercício 22

# Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível.

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