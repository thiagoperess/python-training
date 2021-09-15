# Exercício 23

# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

number = float(input('Digite o número: '))

print('é inteiro.' if number == round(number) else 'é decimal.')

