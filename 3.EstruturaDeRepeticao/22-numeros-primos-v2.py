# Exercício 22

# Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível.

count = 0
divide = []
num = int(input('Digite um número: '))

for i in range(1, num + 1):

    if num % i == 0:
        divide.append(i)

    else:
        count += 1
        
print(f'Divisores de {num}: {divide}')
    
print(f'{num} é primo.' if count == 2 else f'{num} não é primo.')
