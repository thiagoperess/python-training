# Exercício 12

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58:

height = float(input('Digite sua altura: '))
idealWeight = (72.7 * height) - 58
print(f'O peso ideal para {height:.2f}: \
{idealWeight:.2f}Kg.')
