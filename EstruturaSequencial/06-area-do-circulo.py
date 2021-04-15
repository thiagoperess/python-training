# Exercício 06

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

while True:
    radius = float(input('Digite o raio do círculo: '))
    pi = 3.14
    area = pi * (radius ** 2)
    print(f'A área do círculo é {area:.2f}m².')
    option = str(input('Deseja continuar? {S/N] ')).upper()
    print('-' * 30)
    if option not in 'S':
        break
print('Muito obrigado e até a próxima!!')
