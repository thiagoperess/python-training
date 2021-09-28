# Exercício 10

# Faça um programa que receba dois números e gere uma lis dos números que estão no intervalo compreendido por eles.

# Solução:

var1 = int(input('Início: '))+1
var2 = int(input('Fim: '))
lista = []

for i in range(var1, var2):
    lista.append(i)

print(lista)
