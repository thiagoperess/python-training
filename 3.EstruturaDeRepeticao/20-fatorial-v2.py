# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
# e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    num = int(input('Digite um número: '))
    count = num
    fat = 1
    
    if num > 0 and num < 16:
        print(f'Calculando {num}!')

        while count > 0:
            print(f'{count}', end='')
            print(' x ' if count > 1 else ' = ', end='')
            fat *= count
            count -= 1
        
        print(f'{fat}')

        answer = str(input('Deseja continuar? [S/N] '))

        if answer in 's':  
            pass
        
        else:
            print('Até logo')
            break
    else:
        print('Somente entre 0 e 15!!')