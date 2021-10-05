# Exercício 19

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
qty_num = int(input('Quantidade de números: '))

for i in range(qty_num):
    nums = int(input(f'Digite o {i+1}º número: '))

    while nums < 0 or nums > 1000:
        nums = int(input(f'ERRO!! Digite o {i+1}º número: '))
    else:
         lista.append(nums)

print(f'''

O maior número é {max(lista)}
O menor número é {min(lista)}
E sua soma total é {sum(lista)}

''')
