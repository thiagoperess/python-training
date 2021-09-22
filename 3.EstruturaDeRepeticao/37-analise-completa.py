# Exercício 37

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
# + baixo, + gordo e + magro, além da média das alturas e dos pesos dos clientes

cods = []
heights = []
weights = []
num = 1
code = True

while code != 0:
    print(f'Cliente nº {num}')
    code = int(input('Digite o código: '))
    
    if code == 0:
        break
    else:
        height = float(input('Digite a altura: '))
        weight = float(input('Digite o peso: '))
        cods.append(code)
        heights.append(height)
        weights.append(weight)
        num += 1

thin = weights.index(min(weights))
fat = weights.index(max(weights))
tall = heights.index(max(heights))
short = heights.index(min(heights))

print(
    f'Código + magro: {cods[thin]}\n'
    f'Código + gordo: {cods[fat]}\n'
    f'Código + alto: {cods[tall]}\n'
    f'Código + baixo: {cods[short]}\n'
    f'Média altura: {sum(heights) / len(heights):.2f}\n'
    f'Média peso: {sum(weights) / len(weights):.2f}'
    )