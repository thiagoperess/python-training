# Exercício 19 

# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. 

# Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


num = int(input('Digite um número menor que 1000: '))

unity = num // 1 % 10
ten = num // 10 % 10 
hundred = num // 100 % 10
thousand = num // 1000 % 10

print(f'Analisando o número {num} temos:')

print(f'{unity} unidades, \
        {ten} dezenas, \
        {hundred} centenas e \
        {thousand} milhares.')
