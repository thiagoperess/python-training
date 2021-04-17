# Exercício 04

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
for n in range(1,5):
    nota = float(input(f'Nota {n}: '))
    notas.append(nota) 
media = sum(notas) / n
print(f'A soma das notas foi: {sum(notas):.1f}')
print(f'E sua média final foi: {media:.1f}')

