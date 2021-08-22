# Exercício 19

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

list1 = []
len_list1 = int(input('Tamanho da lista: '))

for i in range(len_list1):
    nums = int(input(f'Digite o {i+1}º número: '))

    while nums < 0 or nums > 1000:
        nums = int(input(f'ERRO!! Digite o {i+1}º número: '))
    else:
        list1.append(nums)

print(f'''
       O maior número é {max(list1)}
       O menor número é {min(list1)}
       E sua soma total é {sum(list1)}
       ''')
