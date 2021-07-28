# Exercício 10

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# Solução:

num1 = int(input('Início do intervalo: '))
num2 = int(input('Final do intervalo: '))

for i in range(num1+1,num2):
    print(i)
