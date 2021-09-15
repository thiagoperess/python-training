# Exercício 026

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# Até 20 litros, desconto de 3%
# Acima de 20 litros, desconto de 5%

# Gasolina:
# Até 20 litros, desconto de 4%
# Acima de 20 litros, desconto de 6%
 
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: 
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago 
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# e o preço do litro do álcool é R$ 1,90. 

liters = int(input('Quantos litros? '))
fuel = str(input('Combustível: G [Gasolina] | A [Álcool]: ')).upper().strip()
total = 0
gas = 2.50
alcohol = 1.90
disc = 0

if fuel == 'G':
    total = liters * gas
    fuel = 'Gasolina'

elif fuel == 'A':
    total = liters * alcohol
    fuel = 'Álcool'

for i in range(liters):

    if liters <= 20 and fuel == 'Gasolina':
        disc = total * 0.04
    elif liters > 20 and fuel == 'Gasolina':
        disc = total * 0.06

    elif liters <= 20 and fuel == 'Álcool':
        disc = total * 0.03
    elif liters > 20 and fuel == 'Álcool':
        disc = total * 0.05

final = total - disc

print(f'Abastecido: {liters}L de {fuel}\n'
      f'Total: R$ {total:.2f}.\n'
      f'Desconto: R$ {disc:.2f}.\n'
      f'Total c/ Desconto: R$ {final:.2f}\n')


