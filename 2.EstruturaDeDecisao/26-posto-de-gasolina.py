# Exercício 026

# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# Até 20 litros, desconto de 3% por litro
# Acima de 20 litros, desconto de 5% por litro

# Gasolina:
# Até 20 litros, desconto de 4% por litro
# Acima de 20 litros, desconto de 6% por litro.
# 
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: 
# A-álcool, G-gasolina), calcule e imprima o valor a ser pago 
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# e o preço do litro do álcool é R$ 1,90. 

amount_liters = int(input('Quantos litros abastecer? '))
fuel_type = str(input('Qual combustível? \
                     \nDigite: G [Gasolina] | A [Álcool]: ')
                     ).upper().strip()
total = 0
gas_liter = 2.50
alcohol_liter = 1.90

if fuel_type == 'G':
    total = amount_liters * gas_liter
elif fuel_type == 'A':
    total = amount_liters * alcohol_liter

discount = 0
for i in range(amount_liters):
    if amount_liters <= 20:
        discount = total * 4 / 100
    elif amount_liters > 20:
        discount = total * 6 / 100
fuel_type = 'Gasolina'

discount = 0
for i in range(amount_liters):
    if amount_liters <= 20:
        discount = total * 3 / 100
    elif amount_liters > 20:
        discount = total * 5 / 100
fuel_type = 'Álcool'

final_total = total - discount

print(f'''
Você abasteceu {amount_liters} litros de {fuel_type}.
Isso deu um total de R$ {total:.2f}.
Como foram abastecidos {amount_liters} litros, seu desconto é de R$ {discount}.
No final, com desconto, totaliza R$ {final_total:.2f}
''')


