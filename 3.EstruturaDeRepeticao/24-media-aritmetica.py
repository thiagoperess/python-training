# Exercício 24

# Faça um programa que calcule o mostre a média aritmética de N notas.

qty_nts = int(input('Quantas notas vamos calcular? '))

cont = 0
lst = []
for i in range(qty_nts):
    notas = float(input(f'Nota {i+1}: '))
    lst.append(notas)
    cont += 1

media = sum(lst) / cont

print(f'Notas obtidas: {lst}')

if 7 <= media <= 10:
    print(f'Aprovado com média {media:.2f}!')
else:
    print(f'Reprovado com média {media:.2f}!')
