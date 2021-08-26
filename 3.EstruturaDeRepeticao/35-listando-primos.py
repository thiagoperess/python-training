# Exercício 35

# Encontrar números primos é uma tarefa difícil. 
# Faça um programa que gera uma lista dos números primos existentes 
# entre 1 e um número inteiro informado pelo usuário.

num = int(input('Qual número: '))

for num in range(1, num + 1):
    if all(num % i != 0
        for i in range(2, num)):
            print(num, end='\n')
