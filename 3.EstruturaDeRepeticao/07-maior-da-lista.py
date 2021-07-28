# Exercício 07

# Faça um programa que leia 5 números e informe o maior número.

# Solução

list1 = ['Numero 1: ',
         'Numero 2: ', 
         'Numero 3: ', 
         'Numero 4: ', 
         'Numero 5: ']

list2 = []

for i in range(len(list1)):
    print(list1[i], end='')
    
    nums = int(input(''))
    list2.append(nums)
    
print(f'O maior número é {max(list2)}')
