# Exercício 19

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

list1 = []
len_list1 = int(input('Tamanho da lista: '))

count = 0
while len_list1 != count:
    nums = int(input(f'Digite o {count+1}º número: '))

    while nums > 1000 or nums < 0:
        nums = int(input(f'ERRO!! Digite o {count+1}º número: '))
        
    list1.append(nums)
    count += 1

print(f'O maior número é {max(list1)}')
print(f'O menor número é {min(list1)}')