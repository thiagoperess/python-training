# Exercício 39

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
# e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

codList = []
heightList = []
cNum = 1
code = True

while code <= 10:
    print(f'Aluno nº {cNum}')
    code = int(input('Digite o código: '))
    
    if code == 0:
        break
    else:
        height = float(input('Digite a altura: '))
        codList.append(code)
        heightList.append(height)
        cNum += 1

tall = heightList.index(max(heightList))
short = heightList.index(min(heightList))

print(f'Código do mais alto: {codList[tall]}\n'
      f'Código do mais baixo: {codList[short]}\n')