# Exercício 24

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

print('Digite dois números')
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))

opt = int(input('''Qual operação deseja realizar?

1) Soma;
2) Subtração;
3) Multiplicação;
4) Divisão.

>>> '''))

def add(x, y): return x + y
def subt(x, y): return x - y
def mult(x, y): return x * y
def div(x, y): return x / y

while True:
    if opt == 1:
        num = add(n1, n2)

    elif opt == 2:
        num = subt(n1, n2)

    elif opt == 3:
        num = mult(n1, n2)

    elif opt == 4:
        num = div(n1, n2)

    else:
        print('\nOpção Inválida!')
        break

    print(f'Total: {num:.1f}')
    print('É positivo' if num >= 0 else 'É negativo')
    print('É inteiro' if num == round(num) else 'É decimal')
    print('É par' if num % 2 == 0 else 'É ímpar')
    break