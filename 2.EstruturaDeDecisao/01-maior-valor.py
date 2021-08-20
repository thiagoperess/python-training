# Exercício 01

# Faça um Programa que peça dois números e 
# imprima o maior deles.Não usar a função 'max'.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}!')
else:
    print(f'{num2} é maior que {num1}!')
