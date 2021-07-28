# Exercício 05

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

from time import sleep

years = 0
pop_A = int(input('População País A: '))
pop_B = int(input('População País B: '))
grow_A = float(input('Taxa Crescimento País A: '))
grow_B = float(input('Taxa Crescimento País B: '))

while pop_A < pop_B:
    pop_A += pop_A * grow_A
    pop_B += pop_B * grow_B
    years += 1
    print(f'{years}º ano: País A = {pop_A:.0f}; País B = {pop_B:.0f}')
    sleep(0.5)

print(f'O país A passou o B após {years} anos.')