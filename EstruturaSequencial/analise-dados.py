# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#
# o produto do dobro do primeiro com metade do segundo;
# a soma do triplo do primeiro com o terceiro;
# o terceiro elevado ao cubo.

while True:
    numberOne = int(input('Digite o 1º número: '))
    numberTwo = int(input('Digite o 2º número: '))
    numberThree = float(input('Digite o 3º número: '))
    product = (numberOne * 2) * (numberTwo / 2)
    valueSum = numberOne * 3 + numberThree
    thirdCubed = numberThree ** 3
    print(f'O produto entre o dobro de {numberOne} e a metade de {numberTwo} é {product:.0f}.')
    print(f'A soma do triplo de {numberOne} e {numberThree} é {valueSum:.2f}.')
    print(f'O número {numberThree} elevado ao cubo é {thirdCubed:.2f}.')
    option = str(input('Deseja continuar? [S/N] ')).upper()
    if option not in 'S':
        break
print('Até logo mais!!')
