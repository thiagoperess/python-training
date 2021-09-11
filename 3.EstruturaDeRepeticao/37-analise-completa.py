# Exercício 37

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codList = []
heightList = []
weightList = []
cNum = 1
code = True

while code != 0:
    print(f'Cliente nº {cNum}')
    code = int(input('Digite o código: '))
    
    if code == 0:
        break
    else:
        height = float(input('Digite a altura: '))
        weight = float(input('Digite o peso: '))
        codList.append(code)
        heightList.append(height)
        weightList.append(weight)
        cNum += 1

thin = weightList.index(min(weightList))
fat = weightList.index(max(weightList))
tall = heightList.index(max(heightList))
short = heightList.index(min(heightList))

print(
    f'Código do mais magro: {codList[thin]}\n'
    f'Código do mais gordo: {codList[fat]}\n'
    f'Código do mais alto: {codList[tall]}\n'
    f'Código do mais baixo: {codList[short]}\n'
    f'Média de altura: {sum(heightList) / len(heightList):.2f}\n'
    f'Média de peso: {sum(weightList) / len(weightList):.2f}'
    )