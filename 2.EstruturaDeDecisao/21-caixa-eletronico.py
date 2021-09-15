# Exercício 21

# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Valor do Saque: R$ '))
total = saque
total_notas = 0
notas = 100

while True:
    if total >= notas:
        total -= notas
        total_notas += 1
        
    else:
        if total_notas > 0:
            print(f'{total_notas} nota(s) de R$ {notas}')

        elif notas == 100: notas = 50
        elif notas == 50: notas = 20
        elif notas == 20: notas = 10
        elif notas == 10: notas = 5
        elif notas == 5: notas = 1

        total_notas = 0

        if total == 0:
            break