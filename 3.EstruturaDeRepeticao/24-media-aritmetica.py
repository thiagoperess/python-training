# Exercício 24

# Faça um programa que calcule o mostre a média aritmética de N notas.

qty_notas = int(input('Quantas notas calcular? '))

cont = 0
lista = []

for i in range(qty_notas):
    notas = float(input(f'Nota {i+1}: '))
    lista.append(notas)
    cont += 1

media = sum(lista) / cont

print(f'Notas obtidas: {lista}\n'
      f'Calculando média...\n'
      f'{lista[0]} + {lista[1]} + {lista[2]} / {cont} = {media:.2f}')

print(f'Aprovado! Média: {media:.2f}' 
      if 7 <= media <= 10 
      else f'Reprovado! Média: {media:.2f}')
