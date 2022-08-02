# Exercício 06

# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
alunos = 0
medias =[]
nota = 0


for i in range(3):
    print(f'Notas do {i+1}º aluno: ')

    for n in range(4):
        nota = float(input(f'Digite a {n+1} nota: '))
        notas.append(nota)
        
        media = sum(notas) / len(notas)
    
    if media >= 7:
        medias.append(media)
        alunos += 1

print(f'Quantidade de alunos aprovados: {alunos}')

