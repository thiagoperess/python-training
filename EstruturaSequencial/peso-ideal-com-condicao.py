# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#
# Para homens: (72.7*h) - 58;
# Para mulheres: (62.1*h) - 44.7.

height = float(input('Digite sua altura: '))
woman = 'F'
man = 'M'
gender = str(input('Digite seu sexo [F/M]: ')).upper()
while gender not in 'FM':
    gender = str(input('Digite seu sexo [F/M]: ')).upper()
if gender in 'M':
    print(f'Você tem {height:.2f}cm de altura.\n'
          f'O peso ideal para um homem de sua altura é '
          f'{(72.7 * height) - 58:.1f}Kg.')
else:
    print(f'Você tem {height:.2f}cm de altura.\n'
          f'O peso ideal para uma mulher de sua altura é '
          f'{(62.1  * height) - 44.7:.1f}Kg.')
print('Fim')