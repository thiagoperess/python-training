# Exercício 07

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    base = float(input('Digite o valor da base: '))
    area = base ** 2
    print(f'A area é {area}m²')
    option = str(input('Deseja continuar? [S/N] ')).upper()
    print('-' * 30)
    if option not in 'S':
        break
print('Até logo!')
