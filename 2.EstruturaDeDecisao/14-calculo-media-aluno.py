# Exercício 14

# Faça um programa que lê as N notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito

# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero

# O algoritmo deve mostrar na tela as notas, a média, 
# o conceito correspondente e a mensagem:

# “APROVADO” se o conceito for A, B ou C ou
# “REPROVADO” se o conceito for D ou E.


lista = []
qty_notas = int(input('Quantas notas? '))

for i in range(qty_notas):
    notas = int(input(f'Digite a {i+1}ª nota: '))
    lista.append(notas)

media = sum(lista) / len(lista)

print(f'Notas: {lista}\
        Média {media:.1f}')

if 9 <= media <= 10: print('Conceito A.')
elif 7.5 <= media < 9: print('Conceito B.')
elif 6 <= media < 7.5: print('Conceito C.')
elif 4 <= media < 6: print('Conceito D.')
elif media < 4: print('Conceito E.')

print('Aprovado!' if media >= 6 else 'Reprovado!')