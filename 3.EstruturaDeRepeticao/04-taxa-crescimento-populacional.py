# Exercício 04

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Solução

from time import sleep

pop_A, pop_B, years = 80000, 200000, 0
grow_A, grow_B = 0.03, 0.015

while pop_A < pop_B:
    pop_A += pop_A * grow_A
    pop_B += pop_B * grow_B
    years += 1
    print(f'{years}º ano: País A = {pop_A:.0f}; País B = {pop_B:.0f}')
    sleep(1)

print(f'O país A passou o B após {years} anos.')
