# Exercício 05
 
#  Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores. 

numbers, oddList, evenList = [], [], []

for i in range(20):
    num = int(input(f'Digite o {i+1}º número: '))
    numbers.append(num)

    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)

print(
    f'O vetor completo é: {numbers}\n'
    f'O vetor ímpar é: {oddList}\n'
    f'O vetor par é: {evenList}'
    )