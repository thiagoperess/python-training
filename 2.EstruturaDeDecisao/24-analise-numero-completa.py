# Exercício 24

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print('Digite dois números')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))

option = int(input('''Qual operação deseja realizar?

1) Soma;
2) Subtração;
3) Multiplicação;
4) Divisão.

'''))

if option == 1:
    number = num1 + num2
elif option == 2:
    number = num1 - num2
elif option == 3:
    number = num1 * num2
elif option == 4:
    number = num1 / num2
else:
    print('Opção Inválida.')
    exit()

if number >= 0:
    print(f'O número {number} é positivo.')
else:
    print(f'O número {number} é negativo.')

if number == round(number):
    print(f'O número {number:.0f} é inteiro!')
else:
    print(f'O número {number} é decimal!')

if number % 2 == 0:
    print(f'O número {number} é par')
else:
    print(f'O número {number} é ímpar.')