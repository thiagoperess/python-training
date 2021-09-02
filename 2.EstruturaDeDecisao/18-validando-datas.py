# Exercício 18

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

valid = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31: valid = True

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30: valid = True
        
elif mes == 2:
    if ano %  4 == 0 and ano % 100 !=0 or ano % 400 == 0:
        if dia <= 29: valid = True
    elif dia <= 28: valid = True

print('Data válida' if valid else 'Inválida')

# Utilizando datetime

import datetime

dataCorreta = None
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))

try:
    novaData = datetime.datetime(a, m, d)
    dataCorreta = True

except ValueError:
    dataCorreta = False

print(str(dataCorreta))