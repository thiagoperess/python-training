# Exercício 48

# Faça um programa que peça um numero inteiro positivo e em seguida mostre este num invertido.

# Exemplo:

# 12376489
# => 98467321

num = int(input('Entre com o número: '))
print(f'Número informado: {num}')

numInvertido = int(str(num)[::-1])

print (f'Número invertido: {numInvertido}')