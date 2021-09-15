# Exercício 10

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

# Solução:

var1 = int(input('Início: '))
var2 = int(input('Fim: '))

for i in range(var1+1, var2):
    print(i)
