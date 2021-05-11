# Exercício 17

# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

import datetime
year = int(input('Qual o ano deseja analisar? '))
if year == 0:
    year = datetime.date.today().year
if year % 4 == 0 \
        and year % 100 != 0 \
        or year % 400 == 0:
    print(f'O ano de {year} é BISSEXTO!')
else:
    print(f'O ano de {year} não é BISSEXTO!')
