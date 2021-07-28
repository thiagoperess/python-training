# Exercício 08

# Faça um programa que leia 5 números e informe a soma e a média dos números.

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

    average = sum(list2) / len(list2)
    
print(f'A soma dos números totaliza {sum(list2)} e sua média é {average:.0f}')
