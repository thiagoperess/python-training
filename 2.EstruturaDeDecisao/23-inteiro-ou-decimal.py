# Exercício 23

# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

number = float(input('Digite o número: '))

print(f'{number:.0f} é inteiro.' if number == round(number) else f'{number:.2f} é decimal.')

