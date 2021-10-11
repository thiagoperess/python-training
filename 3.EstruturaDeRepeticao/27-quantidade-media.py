# Exercício 27

# Faça um programa que calcule o número médio de estudantes por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de estudantes para cada turma. 
#  As turmas não podem ter mais de 40 estudantes.

import numpy as np

classes = int(input('Quantidade de turmas: '))

total = []
for i in range(classes):
    students = int(input(f'Estudantes da {i+1}ª turma: '))
    
    while students > 40:
        students = int(input(f'Só 40 por turma: '))    
    
    total.append(students)

media = np.mean(total)
print(f'Média de estudantes: {media:.0f}')
