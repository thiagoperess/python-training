# Exercício 14

# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito

# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem:

# “APROVADO” se o conceito for A, B ou C ou
# “REPROVADO” se o conceito for D ou E.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+nota2)/2

print(f'Com media {media}, seu ', end='')

if 9 <= media < 10:
    print('Conceito é A.')
elif 7.5 <= media < 9:
    print('Conceito é B.')
elif 6 <= media < 7.5:
    print('Conceito é C.')
elif 4 <= media < 6:
    print('Conceito é D.')
elif media < 4:
    print('Conceito é E.')

if media >= 6:
    print('APROVADO. PARABÉNS!')
else:
    print('REPROVADO. ESTUDE MAIS!')