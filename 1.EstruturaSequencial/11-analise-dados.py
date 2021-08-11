# Exercício 11

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# 1) o produto do dobro do primeiro com metade do segundo;
# 2) a soma do triplo do primeiro com o terceiro;
# 3) o terceiro elevado ao cubo.

while True:
    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))
    num3 = float(input('Digite o 3º número: '))
    
    res1, res2, res3 = (num1 * 2) * (num2 / 2), num1 * 3 + num3, num3 ** 3

    print(f'''O produto entre o dobro de {num1} e a metade de {num2} é {res1:.0f}.
              A soma do triplo de {num1} e {num3} é {res2:.2f}.
              O número {num3} elevado ao cubo é {res3:.2f}.
              ''')

    option = str(input('Deseja continuar? [S/N] ')).lower()
    if option in 'n':
        break

print('Até logo mais!!')
