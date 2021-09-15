# Exercício 39

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
# e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cods = []
heights = []

for i in range(5):
    print(f'Aluno nº {i+1}')
    code = int(input('Digite o código: '))
    height = float(input('Digite a altura: '))
    cods.append(code)
    heights.append(height)

tall = heights.index(max(heights))
short = heights.index(min(heights))

print(f'Código do mais alto: {cods[tall]}\n'
      f'Código do mais baixo: {cods[short]}\n')