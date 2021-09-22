# Exercício 08

# Faça um programa que leia N números 
# e informe a soma e a média dos números.

# Solução

lista = []
qty_num = int(input('Quantos números? '))

for i in range(qty_num):
    print(f'Número {i+1}: ', end='')
    nums = int(input(''))
    
    lista.append(nums)

average = sum(lista) / len(lista)
    
print(f'Soma total: {sum(lista)}. '
      f'Média: {average:.1f}.')
