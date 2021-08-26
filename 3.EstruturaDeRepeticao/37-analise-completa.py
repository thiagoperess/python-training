# Exercício 37

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

costumers = int(input('Quantos clientes? '))

codList = []
heightList = []
weightList = []

for i in range(costumers):
    print(f'{i+1}º Cliente')
    cod = int(input('Código: '))
    height = float(input('Altura: '))
    weight = float(input('Peso: '))

    codList.append(cod)
    heightList.append(height)
    weightList.append(weight)
