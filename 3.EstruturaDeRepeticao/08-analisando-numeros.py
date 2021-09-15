# Exercício 08

# Faça um programa que leia 5 números 
# e informe a soma e a média dos números.

# Solução

lista = []

for i in range(5):
    print(f'Número {i+1}: ', end='')
    
    nums = int(input(''))
    lista.append(nums)

    average = sum(lista) / len(lista)
    
print(f'Soma total: {sum(lista)}.\
        Média: {average:.0f}')
