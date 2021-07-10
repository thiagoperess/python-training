# Exercício 23

# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

number = float(input('Digite o número: '))
if number == round(number):
    print(f'O número {number:.0f} é inteiro!')
else:
    print(f'O número {number} é decimal!')


