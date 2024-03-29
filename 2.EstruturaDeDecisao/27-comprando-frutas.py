# Exercício 27

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

# Fruta           Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Solução

strawb = int(input('Quantos kg de morango? '))
apple = int(input('Quantos kg de maça? '))

strawb_kg = 2.50 if strawb <= 5 else 2.20

apple_kg = 1.80 if apple <= 5 else 1.50

total = apple * apple_kg + strawb * strawb_kg

print(f'{strawb}Kg de morango: R${strawb * strawb_kg:.2f}\n'
      f'{apple}Kg de maça: R${apple * apple_kg:.2f}\n'
      f'Total: R${total:.2f}.')