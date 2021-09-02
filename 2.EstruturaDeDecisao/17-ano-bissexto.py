# Exercício 17

# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

year = int(input('Qual o ano deseja analisar? '))

print('É Bissexto!' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'Não é Bissexto!')
