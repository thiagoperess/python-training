# Exercício 27

# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
#  As turmas não podem ter mais de 40 alunos.

import numpy as np

classes = int(input('Quantidade de turmas: '))

total_student = []
for i in range(classes):
    alunos = int(input(f'Alunos da {i+1}ª turma: '))
    
    while alunos > 40:
        alunos = int(input(f'Só 40 na {i+1}ª turma: '))    
    
    total_student.append(alunos)

print(total_student)

mean = np.mean(total_student)
print(f'{mean:.2f}')
