# Exercício 14 

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

# Solução

num = 0
odd_list = []
even_list = []

for i in range(10):
    print(f'Digite o {i+1}º número: ')
    num = int(input('Resp: '))
    
    if num % 2 == 0:
       even_list.append(num)
    else:
        odd_list.append(num)

print('\nOs números pares são: \n' + f'{sorted(even_list)}\n' + \
      '\nOs números ímpares são:\n' f'{sorted(odd_list)}')


