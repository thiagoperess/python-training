# Exercício 07

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    base = float(input('Digite a base: '))
    area = base ** 2
    print(f'Area: {area}m²\nDobro: {area * 2}m²')
    option = str(input('Continuar? [S/N] ')).lower()
    if option in 'n':
        break
print('Até logo!')
