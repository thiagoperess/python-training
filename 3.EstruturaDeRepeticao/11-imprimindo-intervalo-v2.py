# Exercício 11

# Altere o programa anterior para mostrar no final a soma dos números.

# Solução

num1 = int(input('Início do intervalo: '))
num2 = int(input('Final do intervalo: '))

list1 = []

for i in range(num1+1,num2):
    print(i, end=', ')
    list1.append(i)

print(f'\nA soma dos valores é {sum(list1)}')
