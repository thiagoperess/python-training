# Exercício 13

# Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

# Solução

num1 = int(input('Qual a base?: '))
ptcy = int(input('Qual a potência? '))

sqrt = num1 ** ptcy

print(f'O número {num1} elavado à {ptcy} é {sqrt}')
