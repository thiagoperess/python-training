# Exercício 27

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

# Fruta           Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Solução


strawberrys = int(input('Quantos kg de morango você deseja? '))
apples = int(input('Quantos kg de maça você deseja? '))

strawberrys_kg = 0
if strawberrys <= 5:
    strawberrys_kg = 2.50
else:
    strawberrys_kg = 2.20

apples_kg = 0
if apples <= 5:
    apples_kg = 1.80
else:
    apples_kg = 1.50

total = apples * apples_kg + strawberrys * strawberrys_kg

print(f'{strawberrys}Kg de morango mais {apples}Kg de maça totaliza R$ {total:.2f}.')