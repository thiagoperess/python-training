# Exercício 17

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
# 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# Comprar apenas latas de 18 litros;
# Comprar apenas galões de 3,6 litros;
# Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho = float(input('Entre com o tamanho da área: '))

litros = tamanho / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco = latas * 80

galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * 25

# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print(f'''Apenas latas de 18 litros: {latas:.0f}, preço: {preco:.2f}
          Apenas galões de 3.6 litros: {galoes:.0f}, preço: {preco2:.2f}''')

print(f'''Mistura: {mistura_lata} latas e {mistura_galao}
          Galões = {((mistura_lata * 80) + (mistura_galao * 25))}''')

